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

#level will be 1 + the max of the levels of the parameters

    def _clc_value(self):
        pass
    def get_current_value(self):
        return self.current_value
    def get_prev_value(self):
        return self.prev_value
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

    ##This is the function we need to fix

    def _update_value(self):
        global updated_nodes

        self.prev_value = self.current_value
        #global updated_vars

        for i in range(len(self.parameters)):

            if self.parameters[i] in updated_vars or self.parameters[i] in updated_nodes :

                self.current_value = self.current_value + self.parameters[i].get_current_value() - self.parameters[i].get_prev_value()


        if self.current_value!=self.prev_value:
            for n in self.dep_nodes:
                if n  not in updated_nodes:
                    updated_nodes.append(n)

        return self.current_value

class Create_product(Create_exp):

    def _clc_value(self):
        self.current_value =1
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() * self.current_value
        return self.current_value

    def _update_value(self):

        global updated_nodes
        self.prev_value = self.current_value

        for i in range(len(self.parameters)):
            if self.parameters[i] in updated_vars or self.parameters[i] in updated_nodes and self.parameters[i].get_prev_value() !=0:
                self.current_value = int(self.current_value * self.parameters[i].get_current_value() / self.parameters[i].get_prev_value())

        if self.current_value!=self.prev_value:
            for n in self.dep_nodes:
                if n  not in updated_nodes:
                    updated_nodes.append(n)

        return self.current_value




def update_tree():
    global updated_vars

    for  u in updated_vars:
        for n in u.dep:
            if n not in updated_nodes:
                updated_nodes.append(n)

    for n in updated_nodes:
#iterate it level by level
#each node each list : 2d array
        #for b in n.dep_nodes:
            n._update_value()


    #clear updated_vars and nodes
    updated_vars.clear()
    updated_nodes.clear()

def init_tree():
    global var_list
    for v in var_list:
        for item in v.dep:
            item._clc_value()
    for e in exps:
        e._clc_value()








