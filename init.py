from nltk.parse.corenlp import CoreNLPDependencyParser


def init():
    global dependency_parser
    dependency_parser = CoreNLPDependencyParser(url='http://localhost:9000')
    return dependency_parser
