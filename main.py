from bayes import calculateBayes
from random_forest import split_dataset
from decisiontree import decisiontree

my_data=[['slashdot','USA','yes','<20','None'],
['google','France','yes','>20','Premium'],
['digg','USA','yes','>20','Basic'],
['kiwitobes','France','yes','>20','Basic'],
['google','UK','no','>20','Premium'],
['(direct)','New Zealand','no','<20','None'],
['(direct)','UK','no','>20','Basic'],
['google','USA','no','>20','Premium'],
['slashdot','France','yes','<20','None'],
['digg','USA','no','<20','None'],
['google','UK','no','<20','None'],
['kiwitobes','UK','no','<20','None'],
['digg','New Zealand','yes','<20','Basic'],
['slashdot','UK','no','>20','None'],
['google','UK','yes','<20','Basic'],
['kiwitobes','France','yes','<20','Basic']]

case = ['kiwitobes','New Zealand','yes','>20']

tree = decisiontree(training_data=my_data)
forest = split_dataset(my_data)
print(str(tree))
print(tree.classify(case)) #KeyError
print(calculateBayes(my_data, case))
print(forest[0])
print(forest[0].classify(case))
print(forest[1])
print(forest[1].classify(case))