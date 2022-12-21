from variable_class import *
#test
#
v0=Generate_default_vars()
print(v0.get_current_value())
v1=Initiate_rand_vars(min=49,max=90, rand_seed=6)
print(v1.get_current_value())
s= tb.calc_sum([v0.get_current_value(),v1.get_current_value()])

v0.make_change(8)
s1=tb.update_sum(s,[v0.get_prev_value()],[v0.get_current_value()])
print(s1)
tb.compare(s1,100)

