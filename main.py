from variable_class import *
from tree_branches import *
import random
#test magic square 3x3
#vars
v=[]

for i in range(9):
    v.append(Create_var(1,9))
for i in range(9):
    v[i].assign_cust_val(i+1)


#random.shuffle(v)

for i in range(9):
    print(v[i].get_current_value())

a=Create_sum([v[0],v[1],v[2]])
b=Create_sum([v[3],v[4],v[5]])
c=Create_sum([v[6],v[7],v[8]])
d=Create_sum([v[0],v[3],v[6]])
e=Create_sum([v[1],v[4],v[7]])
f=Create_sum([v[2],v[5],v[8]])
g=Create_sum([v[0],v[4],v[8]])
h=Create_sum([v[2],v[4],v[6]])
init_tree()
rnd_walk([a,b,c,d,e,f,g,h],v,15,1,9,10000)
#change propagation
#hill climbing, or any greedy algorthm implementation
print("After random walk\n")
print("independents \n")
for i in range(9):

    print(v[i].get_current_value())
print("nodes\n")
print(a.get_current_value())
print(b.get_current_value())
print(c.get_current_value())
print(d.get_current_value())
print(e.get_current_value())
print(f.get_current_value())
print(g.get_current_value())
print(h.get_current_value())



