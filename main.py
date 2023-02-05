from variable_class import *
from tree_branches import *

#trying to solve magic square
v = []
for i in range(9):
    v.append(Create_var(1,9))
    v[i].assign_rands(seed=i)
    print(v[i].get_current_value())

#sum of rows
a = Create_sum([v[0],v[1],v[2]])
b = Create_sum ([v[3], v[4], v[5]])
c = Create_sum ([v[6], v[7], v[8]])
#sum of cols
d = Create_sum ([v[0], v[3], v[6]])
e = Create_sum ([v[1], v[4], v[7]])
f = Create_sum ([v[2], v[5], v[8]])
#sum of diag from left to right
g = Create_sum([v[0],v[4],v[8]])
#sum of diag from right to left
h = Create_sum([v[2],v[4],v[6]])
#initialise tree
init_tree()
print("sum of rows \n")
print(a.get_current_value())
print(b.get_current_value())
print(c.get_current_value())
print("\nsum of cols \n")
print(d.get_current_value())
print(e.get_current_value())
print(f.get_current_value())
print("\nsum of diag (left to right)\n")
print(g.get_current_value())
print("\nsum of diag (right to left) \n")
print(h.get_current_value())