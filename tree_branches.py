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

    def _update_value(self):
        global updated_nodes
        global updated_vars
        self.prev_value = self.current_value
        #global updated_vars
        flag =0
        for i in range(len(self.parameters)):
            if self.parameters[i] in updated_vars or updated_nodes:

                self.current_value = self.current_value + self.parameters[i].get_current_value() - self.parameters[i].get_prev_value()
                flag =1


        if flag ==0 :
            updated_nodes.append(self)



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
        # global updated_vars
        f=0
        for i in range(len(self.parameters)):
            if self.parameters[i].get_prev_value() != 0 :
                self.current_value = int(self.current_value * self.parameters[i].get_current_value() / self.parameters[i].get_prev_value())
                f=1
        if f==0 or self.current_value!=self.prev_value:
            updated_nodes.append(self)


        return self.current_value




def update_tree():
    global updated_vars
    flag =0
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








