from random import randint
from decisiontree import decisiontree

def split_dataset(dataset):
    trees = []
    attrs = list(dataset[0].keys())
    attrs.remove('Result')
    tree_attr_1 = []
    tree_attr_2 = []
    is_tree_1 = True
    while attrs:
        attr = randint(0, len(attrs)-1)
        if is_tree_1:
            tree_attr_1.append(attrs.pop(attr))
        else:
            tree_attr_2.append(attrs.pop(attr))
        is_tree_1 = not is_tree_1
    tree_attr_1.append('Result')
    tree_attr_2.append('Result')
    trees.append(create_tree(dataset, tree_attr_1))
    trees.append(create_tree(dataset, tree_attr_2))
    return trees

def create_tree(dataset, tree_attr):
    #print(tree_attr)
    sub_dataset = []
    for row in dataset:
        attrs = {}
        for key in tree_attr:
            attrs[key] = row[key]
        sub_dataset.append(attrs)
    return decisiontree(training_data=sub_dataset)
	
