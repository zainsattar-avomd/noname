import json, requests, csv
from web3 import Web3
from web3.middleware import geth_poa_middleware
from collections import defaultdict

# Should be converted to environment variables for production use
polygon_rpc_url = "https://polygon-rpc.com"

api_url = "https://api.polygonscan.com/api"
POLYGONSCAN_API_KEY = "MPP1AN1Y31HPCABQJR15IFKXTQDBEBKACS"

ABI_PATH = "abi.json"
contract_address = "0x7C58D971A5dAbd46BC85e81fDAE87b511431452E"
contract_creator = "0x53ea7896579dea3cC223Eb679ec69f5Df1416B0B"

def initialize_web3():
    
    web3 = Web3(Web3.HTTPProvider(polygon_rpc_url))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    
    params = {
       "module": "contract",
       "action": "getabi",
       "address": contract_address,  #Edge activity token address
       "apikey": POLYGONSCAN_API_KEY # Polygonscan API key
    }    
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            abi = json.loads(data["result"])   
    else: #backup abi key
        try:
            with open(ABI_PATH, 'r') as abi_file:
                abi = json.load(abi_file)
        except Exception as e:
            print("Failed to fetch ABI")
            return None
    
    # Initialize contract
    web3.eth.contract(address=contract_address, abi=abi)
    return web3

def fetch_all_transactions(web3):
    try:
        latest_block = web3.eth.block_number
    except Exception as e:
        latest_block = 58555326
    holder_transactions = defaultdict(int)
    
    for i in range(0, latest_block, 10):
        params = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": contract_address,
        "startblock": 0,
        "endblock": i, #web3.eth.block_number,
        "sort": "asc",
        "apikey": POLYGONSCAN_API_KEY
        }
        
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            transactions = response.json().get("result")
        else:
            print("Error", response.status_code, response.text)
        
        if transactions: # Count transactions by each holder
            for tx in transactions:
                if tx['from'] == contract_creator or tx['to'] == contract_creator:
                    continue 
                holder_transactions[tx['from']] += 1
                holder_transactions[tx['to']] += 1

    return holder_transactions

def fetch_transactions(web3):
    try:
        latest_block = web3.eth.block_number
    except Exception as e:
        latest_block = 58555326
    holder_transactions = defaultdict(int)
    
    params = {
    "module": "account",
    "action": "tokentx",
    "contractaddress": contract_address,
    "startblock": 0,
    "endblock": latest_block, #web3.eth.block_number,
    "sort": "asc",
    "apikey": POLYGONSCAN_API_KEY
    }
    
    #limited to 10000 transactions for sanity
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        transactions = response.json().get("result")
    else:
        print("Error", response.status_code, response.text)
    
    if transactions: # Count transactions by each holder
        for tx in transactions:
            if tx['from'] == contract_creator or tx['to'] == contract_creator:
                continue 
            holder_transactions[tx['from']] += 1
            holder_transactions[tx['to']] += 1

    return holder_transactions

# Main function
def main():
    
    web3 = initialize_web3()
    if not web3:
        print(f"web3 not initialized properly")
        return
    
    holder_transactions = fetch_transactions(web3=web3)
    if not holder_transactions:
        print("Transactions not found")
        return
    
    # Save the result to a CSV file
    with open('holder_transactions.csv', 'w', newline='') as csvfile:
        fieldnames = ['Holder', 'Transaction Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        sorted_holder_transactions = sorted(holder_transactions.items(), key=lambda x: x[1], reverse=True)
        top_wallets = sorted_holder_transactions[:5]
        for holder, count in top_wallets:
            writer.writerow({'Holder': holder, 'Transaction Count': count})

    print("Transaction counts by holder saved to 'holder_transactions.csv'")


if __name__ == "__main__":
    main()