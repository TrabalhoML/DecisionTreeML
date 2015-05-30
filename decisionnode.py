class decisionnode:
	def __init__(self, attr=-1, value_node_dic=None, result=None):
		self.attr = attr
		self.value_node_dic = value_node_dic
		self.result = result

	def __str__(self):
		if self.value_node_dic != None:
			dic_str = "{"
			counter = 0
			for key in self.value_node_dic:
				dic_str += key + " : " + str(self.value_node_dic[key]) 
				if counter != len(self.value_node_dic) - 1:
					dic_str += ", "
					counter += 1
			dic_str += "}"
		else:
			dic_str = "None"
		return ("Decision Node: [attr: " + str(self.attr) + ", value_to_node: " + dic_str + ", result: " + str(self.result) + "]")