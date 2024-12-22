import random
import sys
# define a set
s = set()
n = 1000000
N = str(n)

for i in range(1,n+1):
    # generate a number uniformly in [1, 400]
    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    # add the number to the set
    # check if the number is already in the set
    # if it is, generate another number
    while (x, y) in s:
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
    s.add((x, y))

with open('myInputs/inp1000000.vrp', 'w') as file:
    file.write("NAME : custom_input_1million\n")
    file.write("COMMENT : \"input file for vrp\"\n")
    file.write("TYPE : CVRP\n")
    file.write("DIMENSION : " + N + "\n")
    file.write("EDGE_WEIGHT_TYPE : EUC_2D\n")
    file.write("CAPACITY : 10000\n")
    file.write("NODE_COORD_SECTION\n")
    count = 1
    for (x, y) in s:
        file.write(str(count) + ' ' + str(x) + ' ' + str(y)+ '\n')
        count += 1
    file.write("DEMAND_SECTION\n")
    for i in range(1, n+1):
        file.write(str(i) + ' ' + str(random.randint(1, 500)) + '\n')
    file.write("DEPOT_SECTION\n")
    file.write("0\n")
    file.write("0\n")
    file.write("EOF")