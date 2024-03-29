from typing import List

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean


# D = 2    # dim
# N = 100  # data points
# K = 10   # hash functions
# L = 5    # hash tables

D = 2    # dim
N = 8  # data points
K = 10   # hash functions
L = 2    # hash tables

docs = (np.random.rand(N, D) - 0.5) * 2
docs = np.append(docs, [[1, 1], [1, 0.99]], axis=0)
print(docs)
# plot = plt.scatter([xx[0] for xx in docs], [xx[1] for xx in docs])
# plt.show()

hash_functions = (np.random.rand(L, K, D) - 0.5) * 2

hash_tables = []
for i in range(len(hash_functions)):
    hash_table = {}
    table_functions = hash_functions[i]

    for j in range(len(docs)):
        doc = docs[j]
        doc_bits = ''.join(['1' if x > 0 else '0' for x in np.dot(table_functions, doc)])
        if doc_bits in hash_table:
            hash_table[doc_bits] = hash_table[doc_bits] + [j]
        else:
            hash_table[doc_bits] = [j]

    hash_tables.append(hash_table)

print()
print(hash_tables)


def find_duplicates(doc: List[float], distance_threshold: float = 0.1):
    collisions = []
    for i in range(len(hash_functions)):
        hash_table = hash_tables[i]
        table_functions = hash_functions[i]
        doc_bits = ''.join(['1' if x > 0 else '0' for x in np.dot(table_functions, doc)])
        collisions.extend(hash_table[doc_bits])
    potential_dupes = set(collisions)
    distances = {}
    for potential_dupe in potential_dupes:
        distance = euclidean(doc, docs[potential_dupe])
        print(distance)
        if distance < distance_threshold:
            distances[potential_dupe] = {'distance': distance, 'doc': docs[potential_dupe]}
    return distances


dupes = find_duplicates(docs[9], 0.2)
print()
print(dupes)
