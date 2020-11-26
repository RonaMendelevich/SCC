import numpy as np
import numpy.random
import random


def random_graph(nodes,edges):

    nums = []
    total = edges
    #print('total is:' + total)
    temp = []
    for i in range(nodes-1):
        val = np.random.randint(0, (nodes-1))
        #print('val:')
        #print(val)
        temp.append(val)
        total -= val
    temp.append(total)
    nums.append(temp)
    nums1 = nums[0]

    return nums1

#random.sample(range(100), 10)


#main code
input_a = input("How many nodes?")
nodes = int(input_a)
input_b = input("How many edges?")
edges = int(input_b)
f = open("writescc.txt.txt", "w+")
nums = random_graph(nodes,edges)
print(nums)

for i in range(nodes):
    #print("nums[i] is:")
    #print(nums[i])
    counter = nums[i]
    node1 = i + 1
    if counter != 0:
        for y in range(counter):
            node2 = node1
            #while node2 is node1:
            r = random.sample(range(nodes), counter)
            print(r)
                #for z in r:
                    #while r[z] == node1:
                        #r[z] = random.randint(1, nodes)
                #node2 = random.randint(1, nodes)
            b = str(node2)
            a = str(node1)
            print("node1 is:")
            print(node1)
            print("node2 is:")
            print(node2)
            f.write(a + ' ' + b + '\n')


