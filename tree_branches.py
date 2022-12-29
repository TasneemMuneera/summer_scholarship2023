from variable_class import *
class Create_exp():
    def __init__(self, sum_lst):
        self.parameters = sum_lst
        self.prev_value = None
        self.current_value = 0
        self.future_value = None
        for i in range(len(sum_lst)):
                self.parameters[i].dependents(self)



    def clc_value(self):
        pass
    def get_current_value(self):
        return self.current_value

class Create_sum(Create_exp):

    def clc_value(self):
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() + self.current_value
        return self.current_value


        #return self.current_value

class Create_product(Create_exp):

    def clc_value(self):
        self.current_value =1
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() * self.current_value
        return self.current_value







# def calc_sum(sum_list =[]):
#  # you have to give your chosen values as a list
#   total_sum = 0
#   for i in range(len(sum_list)):
#     total_sum = total_sum + sum_list[i]
#
#   return total_sum
#
# def update_sum(current_sum,old_list, new_list ):
#     for i in range(len(old_list)):
#         current_sum = current_sum - old_list[i] + new_list[i]
#
#     return current_sum
# def compare (value, const):
#     if value != const:
#         if value > const:
#             a= value - const
#             print('exceeded by {}'.format(a))
#
#         else:
#             a = const -value
#             print('short by {}'.format(a))
#         return False
#
#
#     else:
#         print('equal')
#         return True
#





