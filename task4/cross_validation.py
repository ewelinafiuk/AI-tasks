from random import randrange

def cross_validation_split(dataset, folds):
    dataset_split = []
    dataset_copy = dataset
    fold_size = int(len(dataset) / folds)
    for _ in range(folds):
        fold = []
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split
 
