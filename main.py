from variable_class import *
from tree_branches import *

#test
#
v0=Create_var(1,5)
v1=Create_var(1,5)
v2= Create_var(1,5)
v0.assign_rands(seed=6)
v1.assign_rands(seed=6)
v2.assign_rands(seed =6)
# print(v0.get_current_value())
# print(v1.get_current_value())
# print(v2.get_current_value())
# print(var_list[0].get_current_value())
# print(var_list[1].get_current_value())
# print(var_list[2].get_current_value())

a=Create_sum([v0,v1])
b=Create_product([v2,v1,v0])
c=Create_product([a,b])
# e=Create_sum([a,c])
# d=Create_product([c,e])
init_tree()
print(a.get_current_value())
print(b.get_current_value())
print(c.get_current_value())
# print(e.get_current_value())
# print(d.get_current_value())
v1.update_var(10)
# print(v1.get_current_value())
#print(updated_vars)
# print(a.update_value())
#v1.update_var(30)
#print(v1.get_current_value())
#print(updated_vars)
#print(a.update_value())
# print(b.get_current_value())
# print(a)
# print(b)
# print(v0.dep)
# print(v1.dep)
update_tree()
# #
# print(updated_nodes)
# print(a)
# print(b)
# print(a.dep_nodes)
# print(b.dep_nodes)
# print(c)

print(a.get_current_value())
print(b.get_current_value())
print(c.get_current_value())



