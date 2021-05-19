class Edge():
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

class Node():
    def __init__(self, variable):
        self.variable = variable
        self.parents = []
        self.children = []
        self.cpt = None

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def get_probability(self, variables, value):
        return self.cpt.get_probability(variables, value)

    def set_probabilities(self, probabilities):
        variables = []
        for node in self.parents:
            variables.append(node.variable)
        self.cpt = CPT(variables, probabilities)
        
class CPT():
    """
    Condicional probability table
    """
    def __init__(self, variables, probabilities):
        if len(variables) > 0:
            self.parent = variables[0]
            self.true_table = CPT(variables[1:len(variables)], probabilities[0:int(len(probabilities)/2)])  
            self.false_table = CPT(variables[1:len(variables)], probabilities[int(len(probabilities)/2):len(probabilities)])
            self.probability = None
        else:
            self.probability = probabilities[0]
            self.parent = None
            self.false_table = None
            self.true_table = None

    def get_probability(self, variables, value):
        if self.parent == None:
            return self.probability if value == True else 1 - self.probability
        current_val = variables.get(self.parent)
        if self.true_table != None and  current_val == True :
                return self.true_table.get_probability(variables, value)
        elif self.true_table != None and  current_val == False:
                return self.false_table.get_probability(variables, value)
        else:
            return self.probability if current_val == True else 1 - self.probability

        