import math
import operator
from decisionnode import decisionnode

def tree_training(rows):
    if len(rows) == 0:
        return None
    attr_values = get_attr_values(rows)
    return train(rows, attr_values)

def train(rows, attr_values):
    result = None
    value_to_node = None
    attr = get_best_attr(rows)
    if attr == None:
        result = get_most_common_result(rows)
    else:
        value_to_node = {}
        node_values = divide_rows_for_attr_values(rows, attr)
        for key in node_values:
            value_to_node[key] = train(node_values[key], attr_values)
        for value in attr_values[attr]:
            if value not in value_to_node:
                value_to_node[value] = decisionnode(None, None, get_most_common_result(rows))
    node = decisionnode(attr, value_to_node, result)
    return node

def get_attr_values(rows):
    attr_values = {}
    for j in list(rows[0].keys()):
        for i in range(0, len(rows)):
            if j not in attr_values:
                attr_values[j] = [rows[i][j]]
            else:    
                attr_values[j].append(rows[i][j])
    return attr_values

def get_most_common_result(rows):
    result_dic = {}
    for i in range(0, len(rows)):
        if rows[i]['Result'] not in result_dic:
            result_dic[rows[i]['Result']] = 1
        else:
            result_dic[rows[i]['Result']] += 1
    return sorted(result_dic.items(), key=operator.itemgetter(1), reverse=True)[0][0]

def get_best_attr(rows):
    most_valuable_attr = None
    max_information_gain = -1
    for key in list(rows[0].keys()):
        if key == 'Result':
            continue
        attr_gain = information_gain(rows, key)
        #print("Attribute of index " + str(key) + " has information gain of " + str(attr_gain))
        if attr_gain > max_information_gain:
            max_information_gain = attr_gain
            most_valuable_attr = key
    #print("The root attribute is " + str(most_valuable_attr))
    if max_information_gain == 0:
        return None
    else:
        return most_valuable_attr

def information_gain(rows, key):
    rows_entropy = entropy(rows)
    values_entropy = 0
    d = divide_rows_for_attr_values(rows, key)
    for k in d:
        values_entropy += entropy(d[k])*(float(len(d[k]))/len(rows))
    return rows_entropy - values_entropy

def entropy(rows):
    entropy = 0
    d = divide_rows_for_attr_values(rows, 'Result')
    for key in d:
        pi = (float(len(d[key]))/len(rows))
        if pi != 0:
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
