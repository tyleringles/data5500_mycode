

import networkx as nx

# the function
def count_nodes(graph):
    """
    Function to count the number of nodes in a given NetworkX graph.
    :param graph: A NetworkX graph
    :return: Number of nodes in the graph
    """
    # count them uppp
    return graph.number_of_nodes()

# make the graph
if __name__ == "__main__":
    G = nx.Graph()  # Create an empty graph
    G.add_nodes_from([1, 2, 3, 4, 5])  # Adding 5 nodes

    # finally print as always
    print("Number of nodes in the graph:", count_nodes(G))  # Expected output: 5
