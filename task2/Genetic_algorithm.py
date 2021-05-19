# Ewelina Fiuk
# WSI zadanie 2.3

import random
import numpy as np
import matplotlib.pyplot as plt


def function(x):
    '''
    function to find global minimum
    '''
    fun = -20 * np.exp(-0.2* np.sqrt(0.5*(np.mean(x*x) + np.mean(x*x)))) - np.exp(0.5*(np.mean(np.cos(2*np.pi*x) + np.mean(np.cos(2*np.pi*x))))) + np.e +20
    return np.mean(x)


def make_population(population_number, variables_number, bits_number):
    return np.random.randint(2, size=(population_number,variables_number*bits_number))

def decode_individual(individual, variables_number, bits_number, a, b):
    variable = np.split(individual, variables_number)
    decoded = []
    for x in variable:
        decoded.append((a + ((b - a) * binary_to_int(x)) / (2 ** bits_number - 1)))
    return np.array(decoded)

def decode_population(population, variables_number, bits_number, a, b):
    decoded = []
    for individual in population:
        decoded.append(decode_individual(individual,variables_number, bits_number, a, b))
    return decoded

def population_values(population, function):
    values = []
    for individual in population:
        values.append(function(individual))
    return values

def get_best(population, evaluated_pop):
    index = min(range(len(evaluated_pop)), key=evaluated_pop.__getitem__) 
    return population[index]

def binary_to_int(bits):
    return int(''.join([str(i) for i in bits]) , 2)

def crossover(population, crossover_rate, bits_number, cross = None):
    for i in range(0, len(population), 2):
        r = random.random()
        if(r < crossover_rate):
            first = list(population[i])
            second = list(population[i + 1])
            if cross == 2:
                new1, new2 = two_points_cross(first, second)
            elif cross == 3:
                new1, new2 = uniform_cross(first, second, bits_number)
            else:
                new1, new2 = one_point_cross(first, second)
            population[i] = np.array(new1)
            population[i+1] = np.array(new2)
    return population

def one_point_cross(first, second):
        point = random.randint(0,len(first))
        temp1 = first[:point] + second[point:]
        temp2 = second[:point] + first[point:]
        return temp1, temp2

def two_points_cross(first, second):
        point_one = random.randint(0,len(first))
        point_two = random.randint(0,len(first))
        temp1 = list(first)
        temp2 = list(second)
        temp1[point_one:point_two] = temp2[point_one:point_two]
        temp2[point_one:point_two] = temp1[point_one:point_two]
        return temp1, temp2

def uniform_cross(first, second, bits_number):
        probability = np.random.rand(bits_number)
        for i in range(len(probability)-2):
            if probability[i] < 0.5:
                temp = first[i]
                first[i] = second[i]
                second[i] = temp
        return first, second

def selection(population, evaluated_pop):
    v = 0
    values = []
    new_population = []
    maximum = max(evaluated_pop)
    for x in evaluated_pop:
        values.append((v, v + (maximum-x)))
        v += (maximum-x)
    for _ in range(len(population)):
        random = np.random.random() * v
        for j in range(len(values)):
            if(random >= values[j][0] and random <= values[j][1]):
                new_population.append(population[j])
    return new_population

def mutate(population, mutation_rate):
    for i, row in enumerate(population):
        for j, col in enumerate(row):
            if random.random() <= mutation_rate:
                population[i][j] = not population[i][j]


def genetic_algorithm(population_number, variables_number, max_iteration, mutation_rate, crossover_rate, a, b, cross=None):

    bits_number = int(np.log2((b-a)/0.001))
    
    population = make_population(population_number,variables_number,bits_number)
    decoded_population = np.array(decode_population(population, variables_number, bits_number, a, b))
    evaluated_population = population_values(decoded_population, function)
    best = get_best(population, evaluated_population)
    best_list = []
    average_list = []

    for _ in range(max_iteration):
    
        population = selection(population,evaluated_population)
        population = crossover(population, crossover_rate, bits_number, cross)
        mutate(population, mutation_rate)

        decoded_population = decode_population(population, variables_number, bits_number, a, b)
        decoded_population = np.array(decoded_population)
        evaluated_population = population_values(decoded_population,function)

        temporary_best = get_best(population, evaluated_population)
        if function(decode_individual(best, variables_number, bits_number, a, b)) > function(decode_individual(temporary_best, variables_number, bits_number, a, b)):
            best = temporary_best

        best_list.append(function(decode_individual(best, variables_number, bits_number, a, b)))
        average_list.append(np.average(evaluated_population))

    print("Best individual is: ", best)
    b = np.array(decode_individual(best,variables_number,bits_number,a,b))
    print("Best decoded individual is: ",b )
    print("Function minimum value is: ", function(b))
    print("Function average value is: ", average_list[-1:])
    print("")


    plt.plot(average_list)
    plt.xlabel('Population number')
    plt.ylabel('Average value')
    plt.title('Change of average individual in population')
    plt.axis([0, max_iteration, min(average_list)-2, max(average_list) + 2])
    plt.show()

    plt.plot(best_list)
    plt.xlabel('Population number')
    plt.ylabel('Best value for population')
    plt.title('Change of best individual in population')
    plt.axis([0,max_iteration, min(best_list)-1, max(best_list)+1])
    plt.show()



if __name__ == "__main__":
    population_number = 300
    variables_number = 2
    max_iteration = 100
    mutation_rate = 0.01
    crossover_rate = 0.5
    a = -1
    b = 1

    print("single crossover\n")
    genetic_algorithm(population_number, variables_number, max_iteration, mutation_rate, crossover_rate, a, b)
    print("two points crossover\n")
    genetic_algorithm(population_number, variables_number, max_iteration, mutation_rate, crossover_rate, a, b, cross = 2)
    print("uniform crossover\n")
    genetic_algorithm(population_number, variables_number, max_iteration, mutation_rate, crossover_rate, a, b, cross = 3)