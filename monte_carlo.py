import networkx as nx
from random import shuffle
import traditional_shapley as tshp

def calculate_shapley_value(g, prob_vals, maxIter=20000):

    """
    This algorithm is based on page 29 of the following paper:
    https://arxiv.org/ftp/arxiv/papers/1402/1402.0567.pdf

    :param g: the graph
    :param prob_vals: a list. it contains the weight of each node in the graph
    :param maxIter: maximum number of iterations. for 6-12 nodes, the value should be near 2000. for 1000 nodes, this value is
    around 200000
    :return:
    """

    ## first block
    n_nodes = len(g)
    node_list = list(range(0, n_nodes))
    shapley_val_list = [0] * n_nodes

    ##second block
    for i in range(0, maxIter):
        shuffle(node_list)
        P = []
        for node in node_list:
            ## forming the subgraph based on the nodes in P
            subgraph2 = nx.Graph()
            if P:
                subgraph2_nodes = P
                subgraph2.add_nodes_from(subgraph2_nodes)
                if len(subgraph2_nodes) > 1:
                    for x in range(0, len(subgraph2_nodes)):
                        for y in range(x + 1, len(subgraph2_nodes)):
                            if g.has_edge(subgraph2_nodes[x], subgraph2_nodes[y]):
                                subgraph2.add_edge(subgraph2_nodes[x], subgraph2_nodes[y])
                map_val2 = tshp.get_map_value(subgraph2, prob_vals)
            else:
                map_val2 = 0
            ## adding extra node to get map value 1
            subgraph2.add_node(node)
            if len(subgraph2) > 1:
                nbrs = set(g.neighbors(node))
                for nbr in nbrs - set([node]):
                    if subgraph2.has_node(nbr):
                        subgraph2.add_edge(node, nbr)
            map_val1 = tshp.get_map_value(subgraph2, prob_vals)
            shapley_val_list[node] += (map_val1 - map_val2)
            P.append(node)

    ## third block
    for i in range(0, n_nodes):
        shapley_val_list[i] = shapley_val_list[i]/float(maxIter)

    ## fourth block
    return shapley_val_list

def main():

    g = nx.read_yaml('graphs/node_10_p_02.yaml')
    max_run = 20
    prob_values = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.2, 0.3]
    print(calculate_shapley_value(g, prob_vals=prob_values, maxIter=max_run))

if __name__ == "__main__":

    main()