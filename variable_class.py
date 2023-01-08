#considering the bottom leaf nodes
#keeps the properties of the variables
import random
import numpy as np
var_list = []
updated_vars =[]

class Create_var:

    def __init__(self,min_v,max_v):
        self.value = None
        self.prev_value = 0
        self.dep = []
        self.min_v = min_v
        self.max_v = max_v



    def update_var(self,v):
        global updated_vars
        self._make_change(v)
        updated_vars.append(self)
        for i in range(len(updated_vars)):
            if updated_vars[i] == self:
                updated_vars[i] = self

        updated_vars = list(set(updated_vars))



    def assign_rands(self, **kwargs):
        self.rnd_seed = kwargs.get('seed', None)
        random.seed(self.rnd_seed)
        self._rand(self.min_v, self.max_v)
        var_list.append(self)
    def get_current_value(self):
       return int(self._current_value())
    def get_prev_value(self):
        return int(self._prev_value())

    def dependents(self,lst):

        self.dep.append(lst)




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



