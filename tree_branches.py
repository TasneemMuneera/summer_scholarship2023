from variable_class import *
exps=[]
updated_nodes =[]
class Create_exp():
    def __init__(self, sum_lst):
        self.parameters = sum_lst
        self.prev_value = 0
        self.current_value = 0
        self.dep_nodes =[]

        for i in range(len(sum_lst)):
                self.parameters[i].dependents(self)
        exps.append(self)



    def _clc_value(self):
        pass
    def get_current_value(self):
        return self.current_value
    def _update_value(self):
        pass
    def dependents(self,lst):

        self.dep_nodes.append(lst)




class Create_sum(Create_exp):

    def _clc_value(self):
        self.current_value =0
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() + self.current_value
        return self.current_value

    def _update_value(self):
        global updated_nodes
        self.prev_value = self.current_value
        #global updated_vars
        for v in  range(len(updated_vars)): #parameters: check which value is changed in the params: only work on that
            self.current_value = self.current_value + updated_vars[v].get_current_value() - updated_vars[v].get_prev_value()
        if self.current_value != self.prev_value:
            updated_nodes.append(self)



        return self.current_value




        #return self.current_value

class Create_product(Create_exp):

    def _clc_value(self):
        self.current_value =1
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() * self.current_value
        return self.current_value

    def _update_value(self):
        global updated_nodes
        self.prev_value = self.current_value
        # global updated_vars
        for v in range(len(updated_vars)):
            self.current_value = int(self.current_value * updated_vars[v].get_current_value() / updated_vars[v].get_prev_value())
        if self.current_value != self.prev_value:
            updated_nodes.append(self)


        return self.current_value




def update_tree():
    global updated_vars
    for  u in updated_vars:
        for d in u.dep:
            d._update_value()

    for n in updated_nodes:
        for b in n.dep_nodes:
            b._update_value()






def init_tree():
    global var_list
    for v in var_list:
        for item in v.dep:
            item._clc_value()
    for e in exps:
        e._clc_value()








