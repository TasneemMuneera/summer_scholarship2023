# all the relational operators :less, less =, >, > =, +, -, abs, ==, != (binary)
class Create_less_than(Create_exp):


    def _clc_value(self):
        #check less
        self.current_value = 0
        for v in range(len(self.parameters)):
            self.current_value = self.parameters[v].get_current_value() + self.current_value
        return self.current_value

    # global clock 0
    # node clock -1
    def _update_value(self):

        global updated_nodes
        global updated_vars

        self.prev_value = self.current_value
        #no need of loop
        #parameter 1 less than the other
        for i in range(len(self.parameters)):

            if self.parameters[i] in updated_vars or self.parameters[i] in updated_nodes:
                self.current_value = self.current_value + self.parameters[i].get_current_value() - self.parameters[
                    i].get_prev_value()

        if self.current_value != self.prev_value:
            for n in self.dep_nodes:
                if n not in updated_nodes:
                    updated_nodes.append(n)

        return self.current_value


