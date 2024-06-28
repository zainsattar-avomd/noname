### Browser-Based Data Visualization

Create a browser-based application that visualizes the distribution of Edge Activity Token holders on the Polygon mainnet. Your application should dynamically fetch data, process it, and display it on a web-based interactive map, showcasing the geographical distribution of token holders. Utilize canvas or SVG for rendering the map.

### Setup
run *npm install* to install all the node modules
run *npm start* to run the react app
open localhost:3000  on your browser to see the results


### Approach

I have researched as much as possible. However, i could not find any information let alone apis that can fetch
token account holders geo location. I believe there is no way for anyone to know where a transaction took place.

The maximum you can do is to scan all the polygon mainnnet nodes and get an estimate of which node first recieved
a transaction information and then acquire the nodes IP to get an estimation of the location.

Hence to complete the task i have skipped the location data and instead focused on displaying a world map with
random points on the map and a hover functionality to display individual countries.

I'm sorry if i misunderstood this task, since my knowledge on block chain is limited and there was no way to 
ask for clarifications.


I have used a basic react app to create the UI.
I have used react-svg-maps to render the maps

You will find another function that can take raw data and then convert it into co ordinates and then into vector
points which can then be displayed on the map. The code is available in MapChart.js this will be the shell for
any api that can retrieve location data for map holders and then with minor modifications you can use it to display 
the points on the world map.