from bayes import calculateBayes
from random_forest import split_dataset
from decisiontree import decisiontree
import numpy
from comitee import comitee
from cross_validation import cross_validation

def convert_dataset_to_dict(dataset, keys):
	new_dataset = []
	for row in dataset:
		row_dict = {}
		for i in range(0,len(row)):
			row_dict[keys[i]] = row[i]
		new_dataset.append(row_dict)
	return new_dataset

#carrega o dataset de um arquivo texto
dataset = numpy.loadtxt("car-data.txt", dtype="str", delimiter=",")
dataset = convert_dataset_to_dict(dataset, [0, 1, 2, 3, 4, 5, "Result"])

print(str(cross_validation(dataset, include_whole_tree=True, forest_size=2)))
