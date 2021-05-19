#Ewelina Fiuk, 304037
import random
from Graphs import Node, Edge

class BayesianNetwork():
    def __init__(self):
        self.variables_map = {}
        self.edges = []
        self.root_nodes = []

    def add_variable(self, variable):
        new_node = Node(variable)
        self.variables_map[variable] = new_node
        self.root_nodes.append(new_node)

    def add_edge(self, cause, effect):
        source = self.variables_map[cause]
        dest = self.variables_map[effect]
        self.edges.append(Edge(source, dest))
        source.add_child(dest)
        dest.add_parent(source)
        if dest in self.root_nodes:
            self.root_nodes.remove(dest)

    def set_probabilities(self, variable, probabilities):
        self.variables_map[variable].set_probabilities(probabilities)


    def gibbs_sampling(self, wanted_variable, given_variables, iterartions):
        not_given_variables = []
        new_variables_map = {}

        #counter of observed values
        counter = [0, 0]

        #set values of given variables and random values for not given variables
        for v in self.variables_map.keys():
            if v in given_variables:
                new_variables_map[v] = given_variables[v]
            else:
                not_given_variables.append(v)
                new_variables_map[v] = random.choice([True, False])

        #Random walk
        for _ in range(1, iterartions): 
            for v in not_given_variables:
                markov_list = self.markov_blanket(self.variables_map[v])
                markov_map = {}
                for mark in markov_list: 
                    markov_map[mark.variable] = new_variables_map[mark.variable]
                alpha_value = self.alpha(markov_map, v)
                if alpha_value <  random.random():
                    new_variables_map[self.variables_map[v].variable] = False
                else:
                    new_variables_map[self.variables_map[v].variable] = True
                if new_variables_map[wanted_variable] is False:
                    counter[1] += 1
                else:
                    counter[0] += 1

        if  counter[0] + counter[1] == 0: 
            return 0
        else:  
            return counter[0]/(counter[0] + counter[1])


    def alpha(self, markov_map, v):
        given_var = {}
        child_prob_false = 1
        child_prob_true = 1
        
        for parent in self.variables_map[v].parents:
            given_var[parent.variable] = markov_map[parent.variable]
        prob_true = self.variables_map[v].get_probability(given_var, True)
        prob_false = self.variables_map[v].get_probability(given_var, False)

        for child in self.variables_map[v].children:
            child_true = {}
            child_false = {}
            for childp in child.parents:
                if childp.variable != self.variables_map[v].variable :
                    child_true[childp.variable] = markov_map[childp.variable]
                    child_false[childp.variable] = markov_map[childp.variable]
                else:
                    child_true[childp.variable] = True
                    child_false[childp.variable] = False
            child_prob_true = prob_true * child.get_probability(child_true, markov_map[child.variable])
            child_prob_false = prob_false * child.get_probability(child_false, markov_map[child.variable])
       
        alpha = 1.0/(prob_true * child_prob_true + prob_false * child_prob_false)
        return alpha * prob_true * child_prob_true


    def markov_blanket(self, node):
        markov = []
        for parent in node.parents:
            markov.append(parent)
        for children in node.children:
            markov.append(children)
            for child_parent in children.parents:
                if child_parent != node or child_parent not in markov:
                    markov.append(child_parent)
        return markov
