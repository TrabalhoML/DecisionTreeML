from bayes import calculateBayes
from random_forest import split_dataset
from decisiontree import decisiontree
import numpy
from sklearn import cross_validation


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

case = {0 : 'kiwitobes', 1 : 'New Zealand', 2 : 'yes', 3 : '>20'}

dataset = numpy.loadtxt("car-data.txt", dtype="str", delimiter=",")

training, test = cross_validation.train_test_split(my_data, test_size=0.2, random_state=1)
training, validation = cross_validation.train_test_split(training, test_size=0.1, random_state=1)

#tree = decisiontree(training_data=my_data)
forest = split_dataset(my_data)
#print(str(tree))
#print(tree.classify(case)) #KeyError
#print(calculateBayes(my_data, case))
# print(forest[0])
print(forest[0].classify(case))
# print(forest[1])
print(forest[1].classify(case))
