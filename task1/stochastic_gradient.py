# WSI task 1

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits import mplot3d

x, y = symbols('x y', real = True)

def derivative_x(x0, y0, function):
    f = diff(function, x)
    return f.subs(x, x0).subs(y, y0)

def derivative_y(x0, y0, function):
    f = diff(function, y)
    return f.subs(x, x0).subs(y, y0)

def gradient(x0, y0, function):
    return np.array([derivative_x(x0, y0, function), derivative_y(x0, y0, function)])

def f_value(x0, y0, function):
    return function.subs(x, x0).subs(y, y0)

def sga(x0, y0, function, num_of_iters, beta):
    '''
    Stochastic Gradient Ascent algorithm
    '''
    x = x0
    y = y0
    xs = []
    ys =[]
    points = []
    function_values = []
    i = 0
    while i < num_of_iters:
        grad = gradient(x, y, function)
        points.append([x,y])
        xs.append(x)
        ys.append(y)
        function_values.append(f_value(points[i][0], points[i][1], function))
        x += grad[0] * beta
        y += grad[1] * beta
        i += 1
    return points, function_values, xs, ys



def make_2d_plot(points, xs, ys):
    plt.figure()
    plt.scatter(xs, ys, label='Data', c="violet", s=6)
    plt.scatter(points[-1:][0][0], points[-1:][0][1], label = "Max point", c="blue")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Stochastic gradient ascent")
    plt.legend()
    plt.show()

def make_3d_plot(function, points, xs, ys ):
    X = np.linspace(-10, 10, 30)
    Y = np.linspace(-10, 10, 30)
    Z = []
    for x0, y0 in zip(X, Y):
            Z.append(function.subs(x, x0).subs(y,y0))
    plt.figure() 
    ax = plt.axes(projection ='3d') 
    ax.plot3D(X, Y, Z, label = "function") 
    ax.scatter(xs, ys, c = "black", s=5)
    ax.scatter(points[-1:][0][0], points[-1:][0][1], label = "Max point", c="red")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Stochastic gradient ascent")
    plt.legend()
    plt.show() 

'''
#Example data1
function1 =  x*x*(y+1) + 2*y*y*y + 5*y*y    #max in 0, -5/3
x0 = 1
y0 = -1
beta = 0.001
number_of_iterations = 2000
points, f_values, xs, ys = sga(x0, y0, function1, number_of_iterations, beta )
print(points[-1:][0][0], points[-1:][0][1])
print(f_values[-1:])
make_2d_plot(points, xs, ys)
make_3d_plot(function1, points, xs, ys)
'''

'''
#Example data 2:
function2 = x*x*x + 3*x*y*y +12*x*y         #max in (-2, -2)  
x0 = -2
y0 = 0
beta = 0.01
number_of_iterations = 1000
points, f_values, xs, ys = sga(x0, y0,function2, number_of_iterations, beta )
print(points[-1:][0])
print(f_values[-1:])
make_2d_plot(points, xs, ys)
make_3d_plot(function2, points, xs, ys)
'''

'''
#Example data 3:
function3 = x*x*x + 3*x*y*y - 15*x - 12*y   #max in -2, -1
x0 = -2
y0 = 0
beta  = 0.1
number_of_iterations = 200
points, f_values, xs, ys = sga(x0, y0,function3, number_of_iterations, beta )
print(points[-1:][0])
print(f_values[-1:])
make_2d_plot(points, xs, ys)
make_3d_plot(function3, points, xs, ys)
'''


#Example data 4:
function4 = x*y - x*x*y - x*y*y             #max in 1/3, 1/3
x0 = 1
y0 = 1
beta  = 0.1
number_of_iterations = 100
points, f_values, xs, ys = sga(x0, y0,function4, number_of_iterations, beta )
print(points[-1:][0])
print(f_values[-1:])
make_2d_plot(points, xs, ys)
make_3d_plot(function4, points, xs, ys)
