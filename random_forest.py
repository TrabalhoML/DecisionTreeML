from random import randint
from decisiontree import decisiontree

def split_dataset(dataset):
	trees = []
	attrs = list(range(0, len(dataset[0])-1))
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
	tree_attr_1.append(len(dataset[0])-1)
	tree_attr_2.append(len(dataset[0])-1)
	trees.append(create_tree(dataset, tree_attr_1))
	trees.append(create_tree(dataset, tree_attr_2))
	return trees

def create_tree(dataset, tree_attr):
	sub_dataset = []
	for row in dataset:
		attrs = []
		for index in tree_attr:
			attrs.append(row[index])
		sub_dataset.append(attrs)
	return decisiontree(training_data=sub_dataset)
	
