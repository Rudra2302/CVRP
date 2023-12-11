import random
# define a set
s = set()

print("NAME : inp1.vrp")
print("COMMENT : input file for vrp")
print("TYPE : CVRP")
print("DIMENSION : 50000")
print("EDGE_WEIGHT_TYPE : EUC_2D")
print("CAPACITY : 500000")
print("NODE_COORD_SECTION")   


for i in range(1,50001):
    # generate a number uniformly in [1, 400]
    x = random.randint(-10000, 10000)
    y = random.randint(-10000, 10000)
    # add the number to the set
    # check if the number is already in the set
    # if it is, generate another number
    while (x, y) in s:
        x = random.randint(-10000, 10000)
        y = random.randint(-10000, 10000)
    s.add((x, y))

# print the set
count = 1
for (x, y) in s:
    print(str(count) + ' ' + str(x) + ' ' + str(y))
    count += 1

print("DEMAND_SECTION")
for i in range(1, 50001):
    print(str(i) + ' ' + str(random.randint(1, 500)))

print("DEPOT_SECTION")
print("0")
print("0")
print("EOF")