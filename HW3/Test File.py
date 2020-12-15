from timeit import default_timer as timer
from RBTree import Node, RedBlackTree
from pyskiplist import SkipList
from SortedArray import SortedArray
from HashTable import HTable
import random

#Params
START_SIZE = 27 # 2^START_SIZE
END_SIZE = 30 # 2^END_SIZE
SEARCH = True # If True, records both insertion and search time, otherwise only records insertion time

def main():

    for n in range(START_SIZE, END_SIZE+1):
        random.seed = 0

        tree = RedBlackTree()
        skiplist = SkipList()
        sortedArr = SortedArray()
        hTable = HTable()

        start = timer()
        for i in range(2**n):
            # Any kind of Data Structure Implementation here
            # tree.add(random.randint(1, 2**30))
            # Skip List: skiplist.insert(random.randint(1, 2**30), 0)
            # Sorted Array: sortedArr.insert(random.randint(1, 2**30))
            hTable.insert(random.randint(1, 2**30))
        end = timer()
        print(f"Time used to insert 2^{n} numbers: {round(end-start, 2)}s")

        if SEARCH:
            start = timer()
            for i in range(10**5):
                # Any kind of Data Structure Implementation here
                # tree.contains(random.randint(1, 2**30))
                # Skip List: skiplist.search(random.randint(1, 2**30))
                # Sorted Array: sortedArr.search(random.randint(1, 2**30))
                hTable.search(random.randint(1, 2**30))
            end = timer()
            print(f"Time used to search 100k numbers: {round(end-start, 2)}s")

if __name__ == "__main__":
    main()