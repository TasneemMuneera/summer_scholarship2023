#considering the bottom leaf nodes
#keeps the properties of the variables
import random
import tree_branches as tb
import numpy as np
c = False
class Variable_class:
    def __init__(self,**kwargs):
        #sending the value
        # the custom default value
        self.value = None
        self.prev_value =None
        #self.temp_value = None

    def make_change(self, value):

        self.prev_value = self.value
        self.value = value
        global c
        c = True

        return c






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



class Generate_default_vars(Variable_class):

    def __init__(self, **kwargs):
        #this method will create the default variables according to the range
        self.cust_val = kwargs.get('cust_val', None)
        if self.cust_val !=None:
                # storing the objects
                 self.value = self.cust_val
        else:
                 self.value =0


class Initiate_rand_vars(Variable_class):
        #this method will initiate variables from randomly from a range (min, max)
        def __init__(self,min, max,**kwargs):
            self.min_val = min
            self.max_val = max
            self.rand_seed =kwargs.get('rand_seed',None)
            random.seed(self.rand_seed)
            self.value = random.randint(self.min_val, self.max_val)


