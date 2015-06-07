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
