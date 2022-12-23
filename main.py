from variable_class import *
from tree_branches import *
import funcs as f
#test
#
v0=Create_var(8,67)
v1=Create_var(45,90)
v0.assign_rands(seed=6)
v1.assign_rands(seed=6)
print(v0.get_current_value())
v1.update_var(10)
print(v1.get_current_value())
print(var_list)
print(updated_vars)
a=Create_sum([v0,v1])
b=Create_product([v0,v1])


