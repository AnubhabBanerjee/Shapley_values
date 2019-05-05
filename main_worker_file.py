import networkx as nx
import fatima as fm
import monte_carlo as mc
import traditional_shapley as tshp
import configparser
import json
import sys


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    graph_path = config['GRAPH']['Path']
    g = nx.read_yaml(graph_path)
    node_weights = json.loads(config.get("GRAPH","NodeWeights"))
    method_index = int(config['METHOD']['MethodIndex'])
    shapley_values = []
    if method_index == 1:
        shapley_values = tshp.calculate_shapley_values(g, node_weights)
    elif method_index == 2:
        shapley_values == mc.calculate_shapley_value(g, node_weights)
    elif method_index == 3:
        shapley_values = fm.calculate_shapley_values(g, node_weights)
    else:
        sys.exit("Method index does not match! Please choose a right one")
    print(shapley_values)

if __name__ == "__main__":

    main()
