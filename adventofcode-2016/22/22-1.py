from itertools import permutations


def is_viable(pair):
    a, b = pair
    return a['used'] != 0 and a['used'] <= b['available']

nodes = []
with open('input.txt', 'r') as fp:
    for row in fp:
        node = row.split()
        nodes.append({
            'name': node[0],
            'size': int(node[1][:-1]),
            'used': int(node[2][:-1]),
            'available': int(node[3][:-1]),
            'used_percentage': node[4][:-1]
        })

print len(filter(is_viable, permutations(nodes, 2)))
