from variable_class import *
from tree_branches import *
import funcs as f
#test
#
v0=Create_var(8,67)
v1=Create_var(45,90)
v2= Create_var(10,30)
v0.assign_rands(seed=6)
v1.assign_rands(seed=6)
v2.assign_rands(seed =6)
print(v0.get_current_value())
print(v2.get_current_value())
v1.update_var(10)
print(v1.get_current_value())
print(var_list)
print(updated_vars)
a=Create_sum([v0,v1])
b=Create_product([v2,v1,v0])
print(a.clc_value())
print(b.clc_value())
print(a)
print(b)
print(v0.dep)
print(v1.dep)




