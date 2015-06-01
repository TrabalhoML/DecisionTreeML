class decisionnode:
    def __init__(self, attr=-1, value_node_dic=None, result=None):
        self.attr = attr
        self.value_node_dic = value_node_dic
        self.result = result

    def __str__(self):
        if self.value_node_dic != None:
            dic_str = "{"
            dic_str += ', '.join([x + ' : ' + str(y) for x, y in \
                    self.value_node_dic.items()])
            dic_str += "}"
        else:
            dic_str = "None"
        return ("Decision Node: [attr: " + str(self.attr) \
                + ", value_to_node: " + dic_str + ", result: " \
                + str(self.result) + "]")
