#considering the bottom leaf nodes
#keeps the properties of the variables
import random
import tree_branches as tb
import numpy as np

class Create_var:
    def __init__(self,min,max):
        #sending the value
        # the custom default value
        self.min = min
        self.max = max
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

    def init_random_values(self, **kwargs):
        self.rnd_seed = kwargs.get('seed',None)
        random.seed(self.rnd_seed)
        self.value = random.randint(self.min,self.max)



