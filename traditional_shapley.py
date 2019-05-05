from itertools import combinations
import networkx as nx
import math
import graphing

def get_all_subgraphs(graph):

    """
    :param list: a list of items
    :return: all possible combinations of the items
    """
    all_subgraphs = []
    for i in range(1, len(graph.nodes()) + 1):
        for sub_nodes in combinations(graph.nodes(),i):
            subg = graph.subgraph(sub_nodes)
            all_subgraphs.append(subg)
    return all_subgraphs

def get_map_value(subgraph, probabilities):

    """
    :param subgraph: a subgraph of the original graph
    :param probabilities: the user probability array
    :return: the map function as defined by me
    """
    if(nx.is_connected(subgraph)):
        nodeids = subgraph.nodes
        map_value = 0
        for nodeid in nodeids:
            map_value = map_value + probabilities[nodeid]
        return map_value
    else:
        return 0


def calculate_shapeley_value_each_subgraph(nodeid, graph, subgraph, probabilities):

    """
    :param nodeid: node id of a single node in the graph
    :param graph: the graph object
    :param subgraph: the subgraph object
    :param probabilities: the original user probabilities
    :return: the shapley value of the node
    """
    subgraph_1 = subgraph.copy()
    subgraph_1.add_node(nodeid)
    nbrs = set(graph.neighbors(nodeid))
    for nbr in nbrs - set([nodeid]):
        if subgraph_1.has_node(nbr):
            subgraph_1.add_edge(nodeid, nbr)
    map_value_1 = get_map_value(subgraph_1, probabilities)
    map_value_2 = get_map_value(subgraph, probabilities)
    S = subgraph.number_of_nodes()
    N = graph.number_of_nodes()
    return (math.factorial(S) * math.factorial(N -S -1) * (map_value_1 - map_value_2))/math.factorial(N)

def calculate_shapley_values(grph, user_probabilities):

    g = grph # the graph generated based on the pathloss model
    users = list(range(0, len(g)))

    # now we get all possible subgraphs from the single_run graph
    all_subgraphs = graphing.get_all_subgraphs(g)

    # now for each subgraph, calculate the map and shapeley values
    shapeley_values = []
    for node in users:
        user_shapeley = 0
        for subgraph in all_subgraphs:
            if node not in subgraph:
                shapeley = calculate_shapeley_value_each_subgraph(node, g, subgraph, user_probabilities)
                user_shapeley = user_shapeley + shapeley
        shapeley_values.append(user_shapeley)
    return shapeley_values


