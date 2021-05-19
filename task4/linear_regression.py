from cross_validation import cross_validation_split
import numpy as np
import matplotlib.pyplot as plt 
from read_file import load_csv


def mse(predictions, targets):
    sum1 = 0
    for target, prediction in zip(targets, predictions):
        sum1 += (target-prediction)**2
    return (1/len(targets))*sum1

def r_square(predictions, targets):
    sum1 = 0
    sum2 = 0
    mean_val = sum(predictions)/len(predictions)
    for target, prediction in zip(targets, predictions):
        sum1 += (target-prediction)**2
        sum2 += (target - mean_val)**2
    return 1 - sum1/sum2

def mae(predictions, targets):
    sum1 = 0
    for target, prediction in zip(targets, predictions):
        sum1 += abs(target - prediction)
    return (1/len(targets))*sum1

def descent_gradient(dataset, lr, iterations):
    b0 = 0
    b1 = 0
    x = []
    y = []
    for data in dataset:
        x.append(data[0])
        y.append(data[1])
    x = np.array(x)
    for _ in range(iterations):
        prediction = x*b0 + b1
        dw = (-2/len(x)) * np.sum(x*(y - prediction))
        db = (-2/len(x)) * np.sum(y - prediction)
        b0 = b0 - lr * dw
        b1 = b1 - lr * db
    return [b0, b1]

def plot_regression_line(x, y, b0, b1, xlabel, ylabel, title): 
    x = np.array(x)
    plt.scatter(x, y, color = "lightblue", 
               marker = "o", s = 30) 
    y_pred =  b0*x  + b1
    plt.plot(x, y_pred, color = "pink") 
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel) 
    plt.title(title)
    plt.show() 

def linear_regression(dataset, n_folds, lr, iterations): 
    x = []
    y = []
    for d in dataset:
        x.append(d[0])
        y.append(d[1])

    scores = []   
    mse_values = []
    r_values = []
    mae_values=[]

    folds = cross_validation_split(dataset, n_folds)
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = []
        for row in fold:
            row_copy = list(row)
            test_set.append(row)
            row_copy[-1] = None

        score = descent_gradient(train_set, lr, iterations)
        scores.append(score)

        mse_values.append(mse(score, [row[-1] for row in fold]))
        r_values.append(r_square(score,[row[-1] for row in fold]))
        mae_values.append(mae(score, [row[-1] for row in fold]))

    print("MSE value: ", sum(mse_values)/len(mse_values))
    print("MAE value:", sum(mae_values)/len(mae_values))
    print("R square value: ", sum(r_values)/len(r_values))
    b0=0
    b1=0
    for n in range(n_folds):
        b0+=scores[n][0]
        b1 += scores[n][1]
    b0 = b0/n_folds
    b1 = b1/n_folds

    print("Predicted y = ", b0, "* x + ", b1)
    print()
    return x, y, b0, b1

    

if __name__ == "__main__":
    
    aqua_dataset = load_csv('aquatic_toxicity.csv',3,8)
    nr_of_cross_validation_folds = 5
    learning_rate = 0.001
    iterations = 1000
    x, y, b0, b1 = linear_regression(aqua_dataset, nr_of_cross_validation_folds, learning_rate, iterations)
    plot_regression_line(x, y, b0, b1, "H-055", "LC50", "Linear regression of aquatic toxicity") 

    wine_dataset = load_csv("winequality-red.csv", 2, 11)
    nr_of_cross_validation_folds = 5
    learning_rate = 0.001
    iterations = 10000
    x,y,b0,b1 = linear_regression(wine_dataset, nr_of_cross_validation_folds, learning_rate, iterations)
    plot_regression_line(x,y,b0,b1, "citric acid", "quality", "Linera regression of wine quality")
