from parse import parse, graph_edge_labels
from init import init
from graph import draw_graph, init_graph
global headers
global dep_parser

headers = []

def show_headers_deep():
    global headers

    for header in headers:
        header.show()


def show_headers_label():
    global headers
    print("\n")
    print("ALL HEADER LABELS:")
    for header in headers:
        print(header.label)
    print("\n")


def initialize():
    global dep_parser
    dep_parser = init()


def test(sent):
    global dep_parser, headers
    parse(sent, dependency_parser=dep_parser, headers=headers)




initialize()

test("Google sells Android phones")
test("Apple sells iOS phones")
test("Google is a big tech company")
test("Apple stole the project from Google")
test("Mahershi studied at the University of Regina")


draw_graph(graph_edge_labels)
# show_headers_label()
# show_headers_deep()




