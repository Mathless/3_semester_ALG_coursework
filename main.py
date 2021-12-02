import time
from visualization import visualization
from data_structures.red_black_tree import Tree

if __name__ == '__main__':
    tree = Tree()
    for i in range(50):
        tree.insert(i)
        time.sleep(1)
        visualization.show(tree)
    # for i in range(0):
    #  tree.delete(i)
    # print(tree._minimum(tree.root).val)
    # tree.delete(tree.root)
