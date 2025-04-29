import requests  # I bring in a tool to grab stuff from websites
import networkx as nx  # I bring in a tool to make graphs/networks
import os  # I bring in a tool for working with files and folders
import csv  # I bring in a tool to save info into CSV files
from datetime import datetime  # I bring in a tool to know the current date and time

# I create a new directed graph (where arrows go from one coin to another)
g = nx.DiGraph()

# I list the coins I care about, giving them short names
coin_ids = {
    'ethereum': 'eth',
    'bitcoin': 'btc',
    'litecoin': 'ltc',
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'solana': 'sol',
    'dogecoin': 'doge',
    'polkadot': 'dot',
    'tron': 'trx',
    'chainlink': 'link',
    'stellar': 'xlm'
}

# I set up the URL where I ask for prices
url = "https://api.coingecko.com/api/v3/simple/price"
# I set up which coins I want prices for and in what currencies
params = {
    "ids": ",".join(coin_ids.keys()),
    "vs_currencies": ",".join(coin_ids.values())
}

# I send the request to CoinGecko with the above setup
response = requests.get(url, params=params)
# I turn the reply into a Python dictionary I can use
prices = response.json()

# I go through each "from" coin
for from_coin, from_symbol in coin_ids.items():
    # I go through each "to" coin
    for to_symbol in coin_ids.values():
        if from_symbol != to_symbol:  # I skip if it's the same coin (no self-loop)
            try:
                # I get the price from one coin to another
                rate = prices[from_coin][to_symbol]
                # I add an arrow in the graph showing this exchange rate
                g.add_weighted_edges_from([(from_symbol, to_symbol, rate)])
            except KeyError:
                # If the price wasn't available, I just skip
                continue

# If a folder called "data" does not exist yet
if not os.path.exists('data'):
    # I make the "data" folder
    os.makedirs('data')

# I create a timestamp for when I'm saving this
timestamp = datetime.now().strftime('%Y.%m.%d-%H.%M')
# I make a filename with the timestamp inside the "data" folder
filename = f"data/currency_pair_{timestamp}.csv"

# I open that file so I can write into it
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)  # I set up the CSV writer
    writer.writerow(['currency_from', 'currency_to', 'exchange_rate'])  # I write the headers
    # For each arrow (edge) in the graph
    for from_coin, to_coin, data in g.edges(data=True):
        # I write one row: from what coin, to what coin, and the rate
        writer.writerow([from_coin, to_coin, data['weight']])

# PAPER TRADING: I pretend to start with $1000 to test if I can profit
starting_balance = 1000  # I start with $1000 (in Bitcoin)
balances = {coin: 0 for coin in g.nodes}  # I set up empty balances for all coins
balances['btc'] = starting_balance  # I set Bitcoin balance to $1000

# I set variables to track best and worst trade paths
max_factor = 1.0  # Best multiplier found (starts at 1 = no gain)
min_factor = float('inf')  # Worst multiplier found (starts at infinity)
max_paths = ([], [])  # I store the paths for the best trade
min_paths = ([], [])  # I store the paths for the worst trade

# I try every pair of coins (start and end coins)
for coin1 in g.nodes:
    for coin2 in g.nodes:
        if coin1 != coin2:  # I don't trade a coin into itself
            try:
                # I find all simple paths from coin1 to coin2
                for path1 in nx.all_simple_paths(g, coin1, coin2):
                    # I find all simple paths back from coin2 to coin1
                    for path2 in nx.all_simple_paths(g, coin2, coin1):
                        weight1 = 1  # I start the first path weight at 1
                        # I multiply the rates along the first path
                        for i in range(len(path1) - 1):
                            weight1 *= g[path1[i]][path1[i+1]]['weight']

                        weight2 = 1  # I start the second path weight at 1
                        # I multiply the rates along the second path
                        for i in range(len(path2) - 1):
                            weight2 *= g[path2[i]][path2[i+1]]['weight']

                        factor = weight1 * weight2  # I find the total round-trip factor

                        if factor > 1.01:  # If I could make more than 1% profit
                            print("Arbitrage opportunity detected!")
                            print("Path Forward:", path1, "Weight:", weight1)
                            print("Path Reverse:", path2, "Weight:", weight2)
                            print("Factor:", factor)
                            print("Executing Paper Trade...\n")

                            # I simulate doing the trades
                            amount = starting_balance
                            for i in range(len(path1) - 1):
                                rate = g[path1[i]][path1[i+1]]['weight']
                                amount *= rate

                            for i in range(len(path2) - 1):
                                rate = g[path2[i]][path2[i+1]]['weight']
                                amount *= rate

                            profit = amount - starting_balance  # I calculate how much I made
                            print(f"Paper Trade Profit: ${profit:.2f}")
                            print("-" * 30)

                        # I update the biggest profit if needed
                        if factor > max_factor:
                            max_factor = factor
                            max_paths = (path1, path2)
                        # I update the smallest profit if needed
                        if factor < min_factor:
                            min_factor = factor
                            min_paths = (path1, path2)
            except:
                continue  # I ignore any errors (like if no path exists)

# I print the worst trade loop I found
print("Smallest Path weight factor:", min_factor)
print("Paths:", min_paths[0], min_paths[1])
print()
# I print the best trade loop I found
print("Greatest Path weight factor:", max_factor)
print("Paths:", max_paths[0], max_paths[1])
