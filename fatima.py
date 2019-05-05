import random
import networkx as nx
import traditional_shapley as tshp

def calculate_shapley_value_for_single_node(g, prob_vals, node):

    """

    This approach is based on the following paper - https://www.sciencedirect.com/science/article/pii/S0004370208000696?via%3Dihub

    :param g: graph
    :param prob_vals: node weights
    :param node: node under consideration
    :return: shapley value of node under consideration
    """
    users = list(range(0, len(g)))
    users.remove(node)
    no_of_users = len(users)
    shap_val = 0
    for i in range(1, no_of_users+1):
        ulist = random.sample(users, i)
        ## forming the subgraph based on the nodes in P
        subgraph2 = nx.Graph()
        subgraph2_nodes = ulist
        subgraph2.add_nodes_from(subgraph2_nodes)
        if len(subgraph2_nodes) > 1:
            for x in range(0, len(subgraph2_nodes)):
                for y in range(x + 1, len(subgraph2_nodes)):
                    if g.has_edge(subgraph2_nodes[x], subgraph2_nodes[y]):
                        subgraph2.add_edge(subgraph2_nodes[x], subgraph2_nodes[y])
        map_val2 = tshp.get_map_value(subgraph2, prob_vals)
        ## adding extra node to get map value 1
        subgraph2.add_node(node)
        if len(subgraph2) > 1:
            nbrs = set(g.neighbors(node))
            for nbr in nbrs - set([node]):
                if subgraph2.has_node(nbr):
                    subgraph2.add_edge(node, nbr)
        map_val1 = tshp.get_map_value(subgraph2, prob_vals)
        shap_val += (map_val1 - map_val2)

    shap_val = shap_val/ float(no_of_users)

    return shap_val


def calculate_shapley_values(g, prob_vals):

    users = list(range(0, len(g)))
    shap_vals = [0] * len(g)
    for i in users:
        shap_vals[i] = calculate_shapley_value_for_single_node(g, prob_vals, i)
    return shap_vals