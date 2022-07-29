'''
URL for CoreNLPServer: java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
Location for CoreNLPServer: /Users/mahershibhavsar/Downloads/stanford-corenlp-4.4.0
'''


from parse import parse
from init import init
from graph import draw_complete, init_graph, draw_subgraph
from models import Header
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


def parse_trigger(sent):
    global dep_parser, headers
    parse(sent, dependency_parser=dep_parser, headers=headers)


def search_header(word) -> Header:
    global headers
    for header in headers:
        if header.label.lower() == word.lower():
            return header

    return None

'''
Feed new knowledge
'''
def feed_knowledge():
    print("Note: Sentence must be grammatically accurate to produce correct results!")
    print("Text: ", end="")
    x = input()
    parse_trigger(sent=x)


'''
Display entire KG
'''
def show_knowledge_graph():
    draw_complete()


'''
Search for a topic in KG
'''
def search_knowledge_graph():
    print("Available Topics in KG")
    print("(Acquired from Proper Nouns)")
    for header in headers:
        print(header.label, end="; ")

    print("\nSearch Topic: ", end="")
    x = input()
    header = search_header(word=x)
    if header:
        draw_subgraph(header)
    else:
        print("Topic not available")


def exit_control():
    exit()


'''
Main Loop for control options
'''
def run_loop():
    control_map = {
        1: feed_knowledge,
        2: show_knowledge_graph,
        3: search_knowledge_graph,
        0: exit_control
    }

    while True:
        print("Options")
        print("1. Feed Knowledge")
        print("2. View Knowledge Graph")
        print("3. Search in Knowledge Graph")
        print("0. Exit")
        x = int(input())
        if x in control_map.keys():
            control_map[x]()
        else:
            print("Invalid Input!")


initialize()
run_loop()





