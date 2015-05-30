import math

def tree_training(rows):
	tree = None
	most_valuable_attr = -1
	max_information_gain = -1
	for i in range(0, len(rows[0]) - 1):
		attr_gain = information_gain(rows, i)
		print("Attribute of index " + str(i) + " has information gain of " + str(attr_gain))
		if attr_gain > max_information_gain:
			max_information_gain = attr_gain
			most_valuable_attr = i
	print("The root attribute is " + str(most_valuable_attr))

def information_gain(rows, i):
	rows_entropy = entropy(rows)
	values_entropy = 0
	d = divide_rows_for_attr_values(rows, i)
	for key in d:
		values_entropy += entropy(d[key])*(len(d[key])/len(rows))
	return rows_entropy - values_entropy

def entropy(rows):
	entropy = 0
	d = divide_rows_for_attr_values(rows, len(rows[0]) - 1)
	for key in d:
		pi = (len(d[key])/len(rows))
		entropy += pi*math.log(pi, 2)
	return entropy*-1

def divide_rows_for_attr_values(rows, attr):
	dic = {}
	for row in rows:
		if row[attr] not in dic:
			dic[row[attr]] = [row]
		else:
			dic[row[attr]].append(row)
	return dic

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

tree_training(my_data)