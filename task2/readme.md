2. Blockchain Data Interaction

Develop a Node.js application that connects to the Polygon mainnet to fetch transaction histories of the Edge Activity Token holders. Your script should analyze these transactions to identify and display the top 5 most active wallets, excluding the contract creator, by transaction count. Summarize the data in a human-readable format, considering both incoming and outgoing transactions.


Discuss your methodology for filtering and analyzing transaction data, as well as any libraries or frameworks utilized.

## Setup:
create a virtual env using virtualenv im using python3.10
start it with source env/bin/activate
run pip install requirements.txt in the main directory to install dependencies

## Sample command:
python task2.py

## Approach

1. i started off with giving the task to chatgpt and recieving boilerplate code with empty functions
2. i then proceeded to ask multiple questions like what is a contract address, token_address, blocks etc
to gpt to get an idea of how can i approach the problem since i have not worked extensively on blockchain
3. Then i did a detailed exploratory session using google, learning about blockchain, edgeactivity token
, polygon mainnet and available apis that can be used to accomplish this task
4. after my research was complete i decided on using web3 as the main package and read up on its documentation
to understand how can i retrieve transaction data from the sdk
5. then i created an account on polygon scan to use their api and also generated an api_key which i have 
included in the code so you dont have to generate one. It will expire within a month so you will not be able to use 
it later on

6. Then i browsed polygonscan to get edge activity tokens abi, contract token hash, and creator hash so my script
can work properly

7. I then proceeded to code and using all of this information to get to an initial script, After multiple rounds of
testing and debugging i was able to solve the problem.

## Method for filtering and analyzing data

1. i learnt that blocks are immutable and so you can iterate through them one by one to retrieve all the transactions
from them and processing them
2. Keeping this in mind i created a python dictionary that will keep the account holder hash as key and the number of
tx[from] and tx[to] that occur while iterating through each transaction in each block
3. i filtered out the creator token to only count transactions where the creator account was not involved.
4. after checking polygonscan i realized that there were more than 500,000 transactions in total and the polygon scan
api will not allow more than 10000 transactions data per query. This meant the script would take alot of time to process
5. In the script in the code, i have adhered to the 10000 transaction limit and given the results. however, there is
an additional function that will iterate through all the transactions in the block chain
6. To improve efficency i have the following suggestions which are not coded so i will just explain them
7. Since blocks are immutable you can run the functions for each block/or chunks of blocks once and save the results
in a database (im using a csv file for this purpose) You can then write a small script that will sum up transaction data for each account holder for all the blocks. This way, next time you will only have to run the script for blocks
that are not processed before to get the updated results everytime