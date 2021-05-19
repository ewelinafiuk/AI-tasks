#Ewelina Fiuk
#WSI zad 4
from csv import reader

def load_csv(filename, arg1, arg2):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            x = "".join(row)
            dataset.append([float(x.split(";")[arg1]), float(x.split(";")[arg2])])
    return dataset



