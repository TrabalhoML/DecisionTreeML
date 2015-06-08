from bayes import calculateBayes
from random_forest import split_dataset
from decisiontree import decisiontree
import numpy
from sklearn import cross_validation
from comitee import comitee

def convert_dataset_to_dict(dataset, keys):
	new_dataset = []
	for row in dataset:
		row_dict = {}
		for i in range(0,len(row)):
			row_dict[keys[i]] = row[i]
		new_dataset.append(row_dict)
	return new_dataset


my_data=[{0 : 'slashdot', 1 : 'USA', 2 : 'yes', 3 : '<20', 'Result' : 'None'},
{0 : 'google', 1 : 'France', 2 : 'yes', 3 : '>20', 'Result' : 'Premium'},
{0 : 'digg', 1 : 'USA', 2 : 'yes', 3 : '>20', 'Result' : 'Basic'},
{0 : 'kiwitobes', 1 : 'France', 2 : 'yes', 3 : '>20', 'Result' : 'Basic'},
{0 : 'google', 1 : 'UK', 2 : 'no', 3 : '>20', 'Result' : 'Premium'},
{0 : '(direct)', 1 : 'New Zealand', 2 : 'no', 3 : '<20', 'Result' : 'None'},
{0 : '(direct)', 1 : 'UK', 2 : 'no', 3 : '>20', 'Result' : 'Basic'},
{0 : 'google', 1 : 'USA', 2 : 'no', 3 : '>20', 'Result' : 'Premium'},
{0 : 'slashdot', 1 : 'France', 2 : 'yes', 3 : '<20', 'Result' : 'None'},
{0 : 'digg', 1 : 'USA', 2 : 'no', 3 : '<20', 'Result' : 'None'},
{0 : 'google', 1 : 'UK', 2 : 'no', 3 : '<20', 'Result' : 'None'},
{0 : 'kiwitobes', 1 : 'UK', 2 : 'no', 3 : '<20', 'Result' : 'None'},
{0 : 'digg', 1 : 'New Zealand', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'},
{0 : 'slashdot', 1 : 'UK', 2 : 'no', 3 : '>20', 'Result' : 'None'},
{0 : 'google', 1 : 'UK', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'},
{0 : 'kiwitobes', 1 : 'France', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'}]

cases = [{0 : 'kiwitobes', 1 : 'New Zealand', 2 : 'yes', 3 : '>20', 'Result' : 'Premium'},
{0 : 'digg', 1 : 'New Zealand', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'},
{0 : 'slashdot', 1 : 'UK', 2 : 'no', 3 : '>20', 'Result' : 'None'},
{0 : 'google', 1 : 'UK', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'},
{0 : 'kiwitobes', 1 : 'France', 2 : 'yes', 3 : '<20', 'Result' : 'Basic'}]

dataset = numpy.loadtxt("car-data.txt", dtype="str", delimiter=",")
dataset = convert_dataset_to_dict(dataset, [0, 1, 2, 3, 4, 5, "Result"])

training, test = cross_validation.train_test_split(dataset, test_size=0.2, random_state=1)
training, validation = cross_validation.train_test_split(training, test_size=0.1, random_state=1)

case = validation[0]
#my_data = training

# print(validation[0])

tree = decisiontree(training_data=my_data)
forest = split_dataset(my_data, 3)
#print(str(tree))
#print(tree.classify(case)) #KeyError
#print(calculateBayes(my_data, case))
#print("TREE 0: " + str(forest[0]))
#print(forest[0].classify(case))
#print("TREE 1: " + str(forest[1]))
#print("TREE 2: " + str(forest[2]))
#print(forest[1].classify(case))
comitee = comitee(forest, cases)
print(comitee.stacking())
