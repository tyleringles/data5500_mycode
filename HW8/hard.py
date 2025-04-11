

import networkx as nx

# do my funtion
def count_high_degree_nodes(graph):
    """
    Function to count nodes with a degree greater than 5.
    :param graph: A NetworkX graph
    :return: Number of nodes with a degree greater than 5
    """
    # make sum to count
    count = 0

    # make a loop
    for node in graph.nodes():
        if graph.degree(node) > 5:  # Check if degree is greater than 5
            count += 1  # Increase counter

    # count in nodes
    return count

# make graph
if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from(range(10))  # insert my nodes 

#change a few up to spice things up
    G.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])  # Node 0 has degree 7

    # finally print
    print("Number of nodes with degree > 5:", count_high_degree_nodes(G))  # Expected output: 1
