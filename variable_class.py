#considering the bottom leaf nodes
#keeps the properties of the variables

import random

var_list = []
updated_vars =[]
clock_vars =0
class Create_var:

    def __init__(self,min_v,max_v):
        self.value = None
        self.prev_value = 0
        self.dep = []
        self.min_v = min_v
        self.max_v = max_v
        self.level = 0
        self.clock  = -1



    def update_var(self,v):
        global updated_vars
        self._make_change(v)
        #check the clock global and node
        if self.clock==clock_vars:
            updated_vars.append(self)


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
        global clock_vars

        self.prev_value = self.value
        self.value = value
        self.clock = self.clock +1
        clock_vars = self.clock

        #ask
        #clock reset issue check: how many times




    def _current_value(self):
        #will return the current value
        return self.value

    def _prev_value(self):
        #will return the prevoius value
        return self.prev_value

    def _rand(self,min,max):

        self.value = random.randint(min,max)



