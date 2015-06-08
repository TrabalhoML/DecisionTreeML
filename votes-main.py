from bayes import calculateBayes
from cross_validation import cross_validation
from random_forest import split_dataset
from decisiontree import decisiontree
import numpy
from comitee import comitee

def convert_dataset_to_dict(dataset, keys):
	new_dataset = []
	for row in dataset:
		row_dict = {}
		for i in range(0,len(row)):
			row_dict[keys[i]] = row[i]
		new_dataset.append(row_dict)
	return new_dataset


dataset = numpy.loadtxt("votes-data.txt",dtype="str", delimiter=",")
dataset = convert_dataset_to_dict(dataset,["Result",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(str(cross_validation(dataset)))

