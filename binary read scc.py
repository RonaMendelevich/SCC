

def decimalToBinary(n):
    return bin(n).replace("0b", "")


w, h = 3, 3
mat = [[0 for x in range(w)] for y in range(h)]


file = open('fun_bool.txt.txt', 'r')
lines = file.readlines()
bits_num = len(lines)
X = [0 for i in range(bits_num)]
X_next = [0 for i in range(bits_num)]

X[0] = 0
X[1] = 1
X[2] = 1
num_x = 0

print("the X arrays are:")
print(X, X_next)

line_num = 0
for line in lines:
    col_num = 0
    temp = line.strip().split()
    for i in temp:
        mat[line_num][col_num] = i

        col_num += 1

    line_num += 1
print("the matrix is:")
print(mat)
for x in range(line_num):
    # count y (cols)
    counter = 0
    for y in range(col_num):
        # skip the cols we've already been at
        if counter > 0:
            counter -= 1
            continue
        a = mat[x][y]
        a = int(a)
        a1 = X[a-1]
        y += 1
        counter += 1
        print("this is y")
        print(y)
        b = mat[x][y]
        y += 1
        counter += 1
        print("this is y")
        print(y)
        c = mat[x][y]
        c = int(c)
        # if there is one var with no operation
        if c == 0:
            c1 = 0
        else:
            c1 = X[c - 1]

    if b == '|':
        answer = a1 | c1
        print("the answer is:")
        print(answer)
        X_next[x] = (a1 | c1)

    elif b == '&':
        answer = a1 & c1
        print("the answer is:")
        print(answer)
        X_next[x] = (a1 & c1)

    elif b == 0:
        print("the answer is:")
        print(a1)
        X_next[x] = a1

    print(X_next)







