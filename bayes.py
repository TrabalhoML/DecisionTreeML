def calculateBayes(dataset, features):
	classes = {}
	num_attr = len(dataset[0])-1
	classification = {"class": "", "value": 0}
	for row in dataset:
		if row[num_attr] not in classes.keys():
			classes[row[num_attr]] = 1
		else:
			classes[row[num_attr]] += 1
	for attr in classes.keys():
		value = calculateProbability(attr, dataset, features, classes)
		if not classification["class"] or value > classification["value"]:
			classification["class"] = attr
			classification["value"] = value
	return classification["class"]

def calculateProbability(attr, dataset, features, classes):
	result = classes[attr]/float(len(dataset))
	num_attr = len(dataset[0])-1
	for i in range(0, len(features) - 1):
		value = 0
		for row in dataset:
			if row[i] == features[i] and row[num_attr] == attr:
				value += 1
		result *= value/float(classes[attr])
		if result == 0:
			break
	return result