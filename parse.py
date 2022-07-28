from models import Node, Header
from constants import dep_nmod, dep_case, head_edge, header_edge_label, type_reg_node, type_head_node
from graph import graph_obj

global nnp
nnp = set()
graph_edge_labels = {}
node_count = 0
header_node_indexes = []
temp_nodes = {}

def parse(sentence, dependency_parser, headers: list[Header]):
    global nnp
    global graph_edges, graph_edge_labels, node_count, temp_nodes
    parse = dependency_parser.raw_parse(sentence)
    dep = parse.__next__()
    head = Node.create_head()
    prev = head
    prev_dep = None
    temp_nodes = {}
    for i, d in enumerate(list(dep.triples())):
        # print(i)
        print(d)
        if i == 0:
            c = Node(tag=d[0][1], label=d[0][0], prev=prev, next=[], edge=[])

            # print(c)
            # if not cleaning prev sentence from head, it merges
            prev.next = []
            prev.edge = []
            prev.attach(edge=head_edge, node=c)

            # graph_nodes.append({node_count: prev.label})
            # graph_nodes.append({node_count + 1: c.label})
            # graph_edges.append((node_count, node_count+1))
            # graph_edge_labels[(node_count, node_count+1)] = head_edge
            # node_count += 2
            if prev.label not in temp_nodes.keys():
                temp_nodes[prev.label] = node_count
                node_count += 1
            if c.label not in temp_nodes.keys():
                temp_nodes[c.label] = node_count
                node_count += 1

            graph_obj.add_node(temp_nodes[prev.label], **{"label": prev.label, 'type': type_reg_node})
            graph_obj.add_node(temp_nodes[c.label], **{"label": c.label + '\n(' + c.tag + ')', 'type': type_reg_node})
            graph_obj.add_edge(temp_nodes[prev.label], temp_nodes[c.label], label=head_edge)
            # graph_edges.append([prev.label, c.label])
            # graph_edge_labels[(prev.label, c.label)] = head_edge
            prev = prev.next[-1]
            # prev.show()

        while prev.label != d[0][0]:
            prev = prev.prev

        if d[2][1] in tag_handlers.keys():
            tag_handlers[d[2][1]](d[2], head=head, headers=headers)

        if d[1] == dep_nmod:
            prev_nmod = (d[0][0], d[2][0])
        if d[1] == dep_case and prev_dep == dep_nmod:
            nnp.add(prev_nmod[0] + ' ' + d[2][0] + ' ' + prev_nmod[1])
        c = Node(tag=d[2][1], label=d[2][0], prev=prev, next = [], edge=[])
        prev.attach(edge=d[1], node=c)

        if prev.label not in temp_nodes.keys():
            temp_nodes[prev.label] = node_count
            node_count += 1
        if c.label not in temp_nodes.keys():
            temp_nodes[c.label] = node_count
            node_count += 1

        graph_obj.add_node(temp_nodes[prev.label], **{"label": prev.label + '\n(' + prev.tag + ')', 'type': type_reg_node})
        graph_obj.add_node(temp_nodes[c.label], **{"label": c.label + '\n(' + c.tag + ')', 'type': type_reg_node})
        graph_obj.add_edge(temp_nodes[prev.label], temp_nodes[c.label], label=d[1])

        prev_dep = d[1]

        if prev.next:
            prev = prev.next[-1]

    print()
    print(sentence)
    print("TRAVERSE ---------------------------------------------------------")
    head.show()
    print("---------------------------------------------------------")




class Handlers:
    @classmethod
    def add_nnp(cls, pair, head, headers):
        global temp_nodes, node_count
        word = pair[0].lower()
        if word not in nnp:
            nnp.add(word)
            new_header = Header(label=word, next=[])
            headers.append(new_header)
            graph_obj.add_node(node_count, **{"label": new_header.label.upper(), 'type': type_head_node})
            header_node_indexes.append(node_count)
            node_count += 1

        for i, header in enumerate(headers):
            if header.label == word:
                header.attach(head)
                graph_obj.add_edge(temp_nodes[head.label], header_node_indexes[i], label=header_edge_label)

                break




tag_handlers = {
    'NNP': Handlers.add_nnp,
}

# dep_handlers = {
#     'conj': Handlers.conjunction_handler
# }