from nltk.parse.corenlp import CoreNLPDependencyParser

'''
Initialize CoreNLP Server
'''
def init():
    global dependency_parser
    dependency_parser = CoreNLPDependencyParser(url='http://localhost:9000')
    return dependency_parser
