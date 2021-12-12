import math
import numpy as np
import random
import time


import matplotlib.pyplot as plt

from data_structures import red_black_tree, hash_table
from getsize import get_size

#Для разных коэф
#На числах растущих линейно, в разных местах
#

def time_insert_performance(data_stucture, values: list):
    start = time.time()
    for val in values: data_stucture.insert(val)
    end = time.time()
    return end - start


def time_insert_unsorted_performance(data_stucture, values: list):
    start = time.time()
    random.shuffle(values)
    for val in values: data_stucture.insert(val)
    end = time.time()
    return end - start


def size_insert_performance(data_stucture, values: list):
    for val in values: data_stucture.insert(val)
    return get_size(data_stucture)


def time_delete_performance(data_stucture, values: list):
    start = time.time()
    for val in values: data_stucture.delete(val)
    end = time.time()
    return end - start


def draw_insertion_on_sorted_elements():
    sizes = [2 ** i for i in range(4, 15)]
    rb_performance = [time_insert_performance(red_black_tree.Tree(), list(range(size))) for size in sizes]
    ht_performance = [time_insert_performance(hash_table.HashTable(), list(range(size))) for size in sizes]
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title("Insertion performance on sorted elements")
    plt.legend()
    plt.savefig("insertion_sorted.png")
    plt.show()


def draw_insertion_on_sorted_elements_size():
    sizes = [2 ** i for i in range(4, 15)]
    rb_performance = [size_insert_performance(red_black_tree.Tree(), list(range(size))) for size in sizes]
    ht_performance = [size_insert_performance(hash_table.HashTable(), list(range(size))) for size in sizes]
    indices = np.arange(len(sizes))
    print(rb_performance)
    print(ht_performance)
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Size of data stucture")
    plt.title("Insertion size performance on sorted elements")
    plt.legend()
    plt.savefig("insertion_sorted_size.png")

    plt.show()


def draw_delete_on_sorted_elements():
    sizes = [2 ** i for i in range(4, 15)]
    rb_performance = [time_delete_performance(red_black_tree.Tree(list(range(size))), list(range(size))) for size in
                      sizes]
    ht_performance = [time_delete_performance(hash_table.HashTable(list(range(size))), list(range(size))) for size in
                      sizes]
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title("Delete performance on sorted elements")
    plt.legend()
    plt.savefig("delete_sorted.png")

    plt.show()


def draw_delete_on_unsorted_elements(elements="Delete performance on unsorted elements"):
    sizes = [2 ** i for i in range(4, 15)]
    rb_performance = [time_delete_performance(red_black_tree.Tree(get_elements_shuffled(size)),
                                              get_elements_shuffled(size)) for size in sizes]
    ht_performance = [time_delete_performance(hash_table.HashTable(get_elements_shuffled(size)),
                                              get_elements_shuffled(size)) for size in sizes]
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title(elements)
    plt.legend()
    plt.savefig("delete_unsorted.png")

    plt.show()


def get_elements_shuffled(size):
    x = list(range(size))
    random.shuffle(x)
    return x


def draw_insertion_on_unsorted_elements():
    sizes = [2 ** i for i in range(4, 15)]
    rb_performance = [time_insert_unsorted_performance(red_black_tree.Tree(), get_elements_shuffled(size)) for size in
                      sizes]
    ht_performance = [time_insert_unsorted_performance(hash_table.HashTable(), get_elements_shuffled(size)) for size in
                      sizes]
    indices = np.arange(len(sizes))
    width = 0.2
    # Plotting
    plt.bar(indices, rb_performance, width=width, label="Red-black tree")
    # Offsetting by width to shift the bars to the right
    plt.bar(indices + width, ht_performance, width=width, label="Hash table")
    plt.xticks(ticks=indices, labels=["2^" + str(int(math.log2(x))) for x in sizes])
    plt.xlabel("Amount of elements")
    plt.ylabel("Execution time")
    plt.title("Insertion performance on unsorted elements")
    plt.legend()
    plt.savefig("insertion_unsorted.png")
    plt.show()


if __name__ == "__main__":
    start = time.time()
    draw_insertion_on_sorted_elements()
    draw_delete_on_sorted_elements()
    draw_insertion_on_sorted_elements_size()
    draw_insertion_on_unsorted_elements()
    draw_delete_on_unsorted_elements()
    end = time.time()
    print("Графики рисовались:", end - start)
