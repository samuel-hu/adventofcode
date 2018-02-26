from collections import Counter

class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def __repr__(self):
        return '[{} - {}]'.format(self.name, self.weight)

    def __hash__(self):
        return self.name

    def add_child(self, node):
        self.children.append(node)

    def get_weight(self):
        return self.weight + sum([child.get_weight() for child in  self.children])

    def find_imbalanced(self):
        weights = [child.get_weight() for child in self.children]
        most_common = Counter(weights).most_common()

#        print '####################'
#        print self
#        print self.children
#        print weights
#        print '####################'

        if len(most_common) < 2:
            return self, None
        
        imbalanced, offset = self.children[weights.index(most_common[-1][0])].find_imbalanced()
        if offset is None:
            offset = most_common[0][0] - most_common[-1][0]
        return imbalanced, offset
            

def parse_node(node_string):
    name, weight = node_string.split()
    return Node(name, int(weight.strip('()')))

def parse_children(children_string):
    return children_string.split(', ')

def parse_line(line):
    if '->' in line:
        node_string, children_string = line.split('->')
        return parse_node(node_string.strip()), parse_children(children_string.strip())
    else:
        return parse_node(line.strip()), []
        
def build_tree(file_name):
    nodes = {}
    child_to_parent = {} 
    with open(file_name, 'r') as fp:
        for line in fp:
            node, children = parse_line(line)
            nodes[node.name] = node
            for child in children:
                child_to_parent[child] = node.name


    for child, parent in child_to_parent.iteritems():
        nodes[parent].add_child(nodes[child])

    return nodes[(set(nodes.keys()) - set(child_to_parent.keys())).pop()]
            

root = build_tree('input.txt')
imbalanced, offset = root.find_imbalanced()
print 'Node {} off by {}'.format(imbalanced, offset)

