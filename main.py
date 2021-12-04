# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class node:
    def __init__(self, id):
        self.id = id
        self.connected_nodes = []

    def add_connected(self, n):
        self.connected_nodes.append(n)
        n.connected_nodes.append(self)

    def get_children(self,parent, node):
        list=[]
        for n in self.connected_nodes:
            if n != parent:
                list.append(n)
        return list


def load_tree():
    with open('tree.txt', 'r') as file:
        lines, num_nodes = map(int, file.readline().split(' '))
        nodes = [None] * num_nodes

        for i in range(lines):
            id1, id2 = map(int, file.readline().split(' '))
            if not nodes[id1]:
                nodes[id1] = node(id1)
            if not nodes[id2]:
                nodes[id2] = node(id2)
            nodes[id1].add_connected(nodes[id2])
    return nodes


def find_furthest_node(parent, node):

    furthest_node = node
    furthest_distance = -1
    children = node.get_children(parent, node)

    for child in children:
        n, d = find_furthest_node(node, child)
        if d > furthest_distance:
            furthest_distance = d
            furthest_node = n

    return furthest_node, furthest_distance+1


nodes = load_tree()
node1, distance = find_furthest_node(None, nodes[0])
node2, distance = find_furthest_node(None, node1)

print(str(node1.id)+','+str(node2.id)+','+str(distance))
print("%d,%d,%d" % (node1.id, node2.id, distance))
