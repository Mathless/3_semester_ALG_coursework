from time import time
import math
import matplotlib.pyplot as plt
import numpy as np
import time
from data_structures import red_black_tree, hash_table

def time_insert_performance(data_stucture, values: list):
    start = time.time()
    for val in values: data_stucture.insert(val)
    end = time.time()
    return end - start


def time_delete_performance(data_stucture, values: list):
    start = time.time()
    for val in values: data_stucture.delete(val)
    end = time.time()
    return end - start


def draw_insertion_on_sorted_elements():
    sizes = [2 ** i for i in range(4, 12)]
    rb_performance = [time_insert_performance(red_black_tree.Tree(), list(range(size))) for size in sizes]
    ht_performance = [time_insert_performance(hash_table.HashTable(), list(range(size))) for size in sizes]
    # We cannot add width to year so we create another list
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    # Displaying year on top of indices
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title("Insertion performance on sorted elements")
    plt.savefig("insertion_sorted.png")
    plt.legend()
    plt.show()

def draw_delete_on_sorted_elements():
    sizes = [2 ** i for i in range(4, 12)]
    rb_performance = [time_insert_performance(red_black_tree.Tree(list(range(size))), list(range(size))) for size in sizes]
    ht_performance = [time_insert_performance(hash_table.HashTable(list(range(size))), list(range(size))) for size in sizes]
    # We cannot add width to year so we create another list
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    # Displaying year on top of indices
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title("Delete performance on sorted elements")
    plt.savefig("delete_sorted.png")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    start = time.time()
    draw_insertion_on_sorted_elements()
    draw_delete_on_sorted_elements()
    end = time.time()
    print("Графики рисовались:", end-start)
