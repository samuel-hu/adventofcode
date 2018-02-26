# /dev/grid/node-x33-y0     used: 73T
# /dev/grid/node-x0-y14     size: 85T


def print_node(node):
    if node['used'] == 0:
        print '_ ',
    elif node['used'] > 85:
        print '# ',
    elif node['name'] == '/dev/grid/node-x33-y0':
        print 'G ',
    else:
        print '. ',

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

for i, n in enumerate(nodes):
    if not i % 30:
        print
    print_node(n)
