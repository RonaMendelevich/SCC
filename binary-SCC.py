
def next_node(x):
    x33 = x % 10
    x22 = (x % 100) / 10
    x11 = x / 100
    print("x33 is")
    print(x33)
    print("x22 is")
    print(x22)
    print("x11 is")
    print(x11)

    print("now state")
    x3 = int(x33)
    print("x3 is")
    print(x3)
    x2 = int(x22)
    print("x2 is")
    print(x2)
    x1 = int(x11)
    print("x1 is")
    print(x1)
    #print("now state")
    #print(x1, x2, x3)

    x1_new = x2 | x3
    x2_new = x1 & x3
    x3_new = x1
    print("new state")
    print(x1_new, x2_new, x3_new)
    next_state = ((x1_new * 100) + (x2_new * 10) + x3_new)
    print("x1 is:")
    print(x1_new)
    print("next state united:")
    print(next_state)
    return next_state


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(binary):
    decimal = 0
    binary = list(str(binary)) #convert binary to a list
    binary = binary[::-1]      #reverse the list
    power = 0   #declare power variable (for 1st elem == 0)
    for number in binary:
        if number == '1':
            decimal += 2**power
        power += 1 #increase power by 1
    return decimal

nodes = 2**3

graph = {}
graph = dict()
for i in range(nodes):
    graph[i] = []
print(graph)

for i in range(nodes):
    x = i
    xx = decimalToBinary(x)
    print(type(xx))
    int_x = int(xx)
    print(type(int_x))
    print("int_x is: ")
    print(int_x)
    next_x = next_node(int_x)
    dec_next_x = binary_to_decimal(next_x)
    print("new x is: ")
    print(dec_next_x)

    # add to dict
    graph[x].append(dec_next_x)
    print("dict is:")
    print(graph)