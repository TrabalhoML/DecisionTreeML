from random import randint
from decisiontree import decisiontree

def split_dataset(dataset, number_of_trees):
    trees = []
    attrs = list(dataset[0].keys())
    attrs.remove('Result')
    trees_attr = []
    for i in range(0, number_of_trees):
        trees_attr.append([])
    tree_index = 0
    while attrs:
        attr = randint(0, len(attrs)-1)
        trees_attr[tree_index].append(attrs.pop(attr))
        tree_index += 1
        tree_index = tree_index%number_of_trees
    
    for i in range(0, len(trees_attr)):
        trees_attr[i].append('Result')
    for i in range(0, len(trees_attr)):
        trees.append(create_tree(dataset, trees_attr[i]))
    return trees

def create_tree(dataset, tree_attr):
    print(tree_attr)
    sub_dataset = []
    for row in dataset:
        attrs = {}
        for key in tree_attr:
            attrs[key] = row[key]
        sub_dataset.append(attrs)
    return decisiontree(training_data=sub_dataset)
	
