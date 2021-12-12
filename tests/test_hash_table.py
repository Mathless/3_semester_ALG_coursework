import pytest

from data_structures import hash_table


@pytest.mark.parametrize("input", [([]), ([10]), ([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])])
def test_add_and_delete(input):
    ht = hash_table.HashTable()
    for el in input:
        ht.insert(el, el * 10)
        assert ht.get(key=el) == el * 10
    for el in input:
        ht.delete(el)
        assert ht.get(key=el) == None

@pytest.mark.parametrize("input", [(100), (1000), (10000), (100000)])
def test_add_a_lot_of_elements_init(input):
    ht = hash_table.HashTable(list(range(0, input)))
    sizes = [2 ** i for i in range(4, 12)]
    ht = [(hash_table.HashTable(list(range(size))), list(range(size))) for size in sizes]


