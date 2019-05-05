from itertools import combinations

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
