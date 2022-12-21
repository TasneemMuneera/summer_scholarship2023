#considering the bottom leaf nodes
#keeps the properties of the variables
import random
import tree_branches as tb
import numpy as np
var_list = []
class Variable_class:
    def __init__(self):
        #sending the value
        # the custom default value

        self.value = None
        self.prev_value =None
        #self.temp_value = None



    def make_change(self, value):

        self.prev_value = self.value
        self.value = value



    def show_current_value(self):
        #print the current value
        print(self.value)
    def show_previous_value(self):
        #print the previous value
        print(self.prev_value)


    def get_current_value(self):
        #will return the current value
        return self.value

    def get_prev_value(self):
        #will return the prevoius value
        return self.prev_value

    def assign_rand(self, **kwargs):
        self.rnd_seed = kwargs.get('seed',None)
        random.seed(self.rnd_seed)
        self.value = random.randint(self.min_v,self.max_v)


class Create_var(Variable_class):

    def __init__(self,min_v,max_v):
        self.min_v = min_v
        self.max_v = max_v
        self.var =Variable_class()

        var_list.append(self.var)




