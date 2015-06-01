from tree_training import tree_training

class decisiontree:
    def __init__(self,root=None,training_data=None):
        self.root = root
        if training_data:
            self.root = tree_training(training_data)

    def classify(self,features):
        if not self.root:
            raise ValueError("No root or training data is set")
        seek_node = self.root
        while seek_node.result is None:
            try:
                seek_node = seek_node.value_node_dic[features[seek_node.attr]]
            except KeyError:
                raise ValueError(str(features[seek_node.attr]) \
                    + " is not an known value in attribute " \
                    + str(seek_node.attr))
        return seek_node.result

    def __str__(self):
        return str(self.root)


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

tree = decisiontree(training_data=my_data)
print(str(tree))
print(tree.classify(['(direct)','France','yes','>20'])) #KeyError
