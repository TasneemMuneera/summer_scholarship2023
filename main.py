from variable_class import *
from tree_branches import *
import funcs as f
#test
#
v0=Create_var(8,67)
v1=Create_var(45,90)
v0.assign_rand(seed=6)
v1.assign_rand(seed=6)
v0.show_current_value()
v1.show_current_value()
print(var_list)

a=Create_sum([v0,v1])



