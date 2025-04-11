import requests
import networkx as nx

# Create the graph
g = nx.DiGraph()

# track them
coin_ids = {
    'ethereum': 'eth',
    'bitcoin': 'btc',
    'litecoin': 'ltc',
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos'
}

# pull data
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": ",".join(coin_ids.keys()),
    "vs_currencies": ",".join(coin_ids.values())
}

response = requests.get(url, params=params)
prices = response.json()

# outline graph
for from_coin, from_symbol in coin_ids.items():
    for to_symbol in coin_ids.values():
        if from_symbol != to_symbol:
            try:
                rate = prices[from_coin][to_symbol]
                g.add_weighted_edges_from([(from_symbol, to_symbol, rate)])
            except KeyError:
                continue

# Check 
max_factor = 1.0
min_factor = float('inf')
max_paths = ([], [])
min_paths = ([], [])

for coin1 in g.nodes:
    for coin2 in g.nodes:
        if coin1 != coin2:
            try:
                for path1 in nx.all_simple_paths(g, coin1, coin2):
                    for path2 in nx.all_simple_paths(g, coin2, coin1):
                        weight1 = 1
                        for i in range(len(path1) - 1):
                            weight1 *= g[path1[i]][path1[i+1]]['weight']

                        weight2 = 1
                        for i in range(len(path2) - 1):
                            weight2 *= g[path2[i]][path2[i+1]]['weight']

                        factor = weight1 * weight2

                        print("Paths from", coin1, "to", coin2)
                        print("Forward:", path1, weight1)
                        print("Reverse:", path2, weight2)
                        print("Factor:", factor)
                        print()

                        if factor > max_factor:
                            max_factor = factor
                            max_paths = (path1, path2)
                        if factor < min_factor:
                            min_factor = factor
                            min_paths = (path1, path2)
            except:
                continue

print("Smallest Path weight factor:", min_factor)
print("Paths:", min_paths[0], min_paths[1])
print()
print("Greatest Path weight factor:", max_factor)
print("Paths:", max_paths[0], max_paths[1])
