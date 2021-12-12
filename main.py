import time

import data_structures.hash_table
from data_structures import hash_table
from visualization import visualization
from data_structures.red_black_tree import Tree
import random
def get_elements_shuffled(size):
    x = list(range(size))
    random.shuffle(x)
    return x
if __name__ == '__main__':
    # tree = Tree()
    # for i in range(50):
    #     tree.insert(i)
    #     time.sleep(1)
    #     visualization.show(tree)
    start = time.time()
    print(hash_table.HashTable(get_elements_shuffled(64)))
    print("512 el:",time.time() - start)
    start = time.time()
    print(hash_table.HashTable(get_elements_shuffled(128)))
    print("1024 el:", time.time()-start)


    # for i in range(0):
    #  tree.delete(i)
    # print(tree._minimum(tree.root).val)
    # tree.delete(tree.root)
