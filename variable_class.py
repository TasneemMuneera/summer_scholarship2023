#considering the bottom leaf nodes
#keeps the properties of the variables
import random
import tree_branches as tb
import numpy as np
var_list = []
updated_vars =[]
class Variable_class:
    def __init__(self):
        #sending the value
        # the custom default value

        self.value = None
        self.prev_value =None
        #self.temp_value = None



    def _make_change(self, value):

        self.prev_value = self.value
        self.value = value



    def _current_value(self):
        #will return the current value
        return self.value

    def _prev_value(self):
        #will return the prevoius value
        return self.prev_value

    def _rand(self,min,max):

        self.value = random.randint(min,max)


class Create_var(Variable_class):

    def __init__(self,min_v,max_v):
        self.min_v = min_v
        self.max_v = max_v
        self.var =Variable_class()

        var_list.append(self.var)
    def update_var(self,v):
        self.var._make_change(v)
        updated_vars.append(self.var)

    def assign_rands(self, **kwargs):
        self.rnd_seed = kwargs.get('seed', None)
        random.seed(self.rnd_seed)
        self.var._rand(self.min_v, self.max_v)
        updated_vars.append(self.var)
    def get_current_value(self):
       return self.var._current_value()







