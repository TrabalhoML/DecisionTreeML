def calculateBayes(dataset, features):
	classes = {}
	classification = {"class": "", "value": 0}
	for row in dataset:
		if row["Result"] not in classes.keys():
			classes[row["Result"]] = 1
		else:
			classes[row["Result"]] += 1
	for attr in classes.keys():
		value = calculateProbability(attr, dataset, features, classes)
		if not classification["class"] or value > classification["value"]:
			classification["class"] = attr
			classification["value"] = value
	return classification["class"]

def calculateProbability(attr, dataset, features, classes):
	result = classes[attr]/float(len(dataset))
	for i in range(0, len(features) - 1):
		value = 0
		for row in dataset:
			if row[i] == features[i] and row["Result"] == attr:
				value += 1
		result *= value/float(classes[attr])
		if result == 0:
			break
	return result