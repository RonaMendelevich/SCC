import numpy as np
import numpy.random
import random


#main code
input_a = input("How many nodes?")
nodes = int(input_a)
input_b = input("How many edges?")
edges = int(input_b)
f = open("writescc.txt.txt", "w+")
graph = {}
graph = dict()
for i in range(nodes):
    graph[i+1] = []
print(graph)

for i in range(edges):
    # generate 2 random nodes and write to file
    node1 = random.randrange(1, nodes+1)
    print(node1)
    node2 = random.randrange(1, nodes+1)
    while node1 == node2:  # self loop check
        node2 = random.randrange(1, nodes)
    print(node2)
    # for value in graph[node]:
    no2 = str(node2)
    values1 = graph.get(node1)

    if node2 not in values1:
        print("entered")
        graph[node1].append(node2)
        print("dict is:")
        print(graph)
    else:
        print("else")
        i = i + 1