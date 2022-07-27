import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv
from constants import type_head_node, type_reg_node, node_color_map


global graph_obj
graph_obj = nx.Graph()

def init_graph():
    global graph_obj
    graph_obj = nx.Graph()


def draw_graph(edge_labels):
    global graph_obj
    # pos = nx.spring_layout(graph_obj)
    pos = nx.nx_pydot.graphviz_layout(graph_obj, prog='dot')
    plt.figure()
    node_labels = nx.get_node_attributes(graph_obj, 'label')
    node_types = nx.get_node_attributes(graph_obj, 'type')
    colors = [node_color_map[node_type] for node_type in node_types.values()]

    nx.draw_networkx_labels(graph_obj, pos, labels=node_labels,)

    nx.draw_networkx_edge_labels(graph_obj, pos, edge_labels=edge_labels,)
    nx.draw(graph_obj, pos, edge_color='black', width=1.2, with_labels=False, alpha=0.2, node_color=colors)

    nx.drawing.nx_pydot.write_dot(graph_obj, 'result.dot')
    plt.axis('off')
    plt.show()
