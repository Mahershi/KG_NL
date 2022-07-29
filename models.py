from constants import head_tag, head_label


'''
Modal Class for Header Node
'''
class Header:
    next = None
    label = None

    def __init__(self, next=[], label=None):
        self.next = next
        self.label = label

    def attach(self, node):
        self.next.append(node)

    def show(self):
        print("HEADER---------------------------------------------------------------")
        print(self.label)
        for node in self.next:
            node.show()
        print("HEADER END---------------------------------------------------------------")

'''
Modal Class for regular nodes
'''
class Node:
    next = None
    prev = None
    edge = None
    tag = None
    label = None
    # mods = None
    # mod_edge = None

    def __init__(self, prev = None, next=[], edge=[], tag=None, label=None,):
        self.prev = prev
        self.label = label
        self.edge = edge
        self.next = next
        self.tag = tag
        # self.mod = mod
        # self.mod_edge = mod_edge

    @classmethod
    def create_head(cls):
        return cls(tag=head_tag, label=head_label)

    def attach(self, edge, node):
        self.next.append(node)
        self.edge.append(edge)

    # def attach_mod(self, edge, mod_node):
    #     self.mod.append(mod_node)
    #     self.mod_edge.append(edge)

    def show(self):
        if self.prev:
            print("LABEL:", self.label, "\tTAG:", self.tag, "\tPREV:", self.prev.label)
        else:
            print("LABEL:", self.label, "\tTAG:", self.tag, "\tPREV: NONE",)

        for e, n in zip(self.edge, self.next):
            print(e.ljust(15), end="")
            n.show()