import networkx as nx
import matplotlib.pyplot as plt
from constants import type_head_node, type_reg_node, node_color_map, header_edge_label, edge_label_color
from models import Header, Node
import copy

global node_count
global graph_obj
graph_obj = nx.Graph()


'''
Initializes global graph object which holds the entire knowledge graph
'''
def init_graph():
    global graph_obj
    graph_obj = nx.Graph()
    plt.ion()


'''
Draw a subgraph for the header node provided.
It does so by traversing through all the child nodes.
'''
def draw_subgraph(header: Header):
    global node_count
    node_count = 0
    graph = nx.Graph()
    graph.add_node(node_count, **{"label": header.label.upper(), 'type': type_head_node})
    header_node_count = copy.copy(node_count)
    node_count += 1


    for node in header.next:
        graph.add_node(node_count, **{'label': node.label, 'type': type_reg_node})
        graph.add_edge(header_node_count, node_count, label=header_edge_label)
        root_node_index = copy.copy(node_count)
        node_count += 1
        traverse(graph, node, root_node_index)

    '''
    Show the graph generated
    '''
    plot_graph(graph, filename=header.label+'.png')


'''
For a given node head, traverse through its children.
'''
def traverse(graph, head: Node, root_node_index):
    global node_count
    for node, edge in zip(head.next, head.edge):
        graph.add_node(node_count, **{'label': node.label, 'type': type_reg_node})
        graph.add_edge(root_node_index, node_count, label=edge)
        node_count += 1
        traverse(graph, node, copy.copy(node_count-1))


'''
show the graph for the give graph object.
'''
def plot_graph(graph, filename):
    # dot layout
    pos = nx.nx_pydot.graphviz_layout(graph, prog='dot')
    plt.figure()

    # extracting node_labels
    node_labels = nx.get_node_attributes(graph, 'label')
    # extracting node_types for node specific color
    node_types = nx.get_node_attributes(graph, 'type')
    # generating color array based on node_type
    colors = [node_color_map[node_type] for node_type in node_types.values()]
    edge_labels = nx.get_edge_attributes(graph, 'label')
    # adding node lables
    nx.draw_networkx_labels(graph, pos, labels=node_labels, )
    # adding edge_labels
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, horizontalalignment='left', rotate=True, font_color=edge_label_color)
    nx.draw(graph, pos, edge_color='black', width=1.2, with_labels=False, alpha=0.2, node_color=colors)
    # store the graph data to a .dot file
    nx.drawing.nx_pydot.write_dot(graph, 'result.dot')
    plt.axis('off')
    # open graph window
    plt.show()

    # plt.savefig(filename)


'''
Draw the graph for the global graph object which holds entire KG
'''
def draw_complete():
    plot_graph(graph_obj, filename='complete.png')
