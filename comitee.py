from decisiontree import decisiontree
import operator

class comitee:
    def __init__(self, decision_tree_list=None, validation_data=None):
        self.decision_tree_list = decision_tree_list
        self.validation_data = validation_data

    def weighted_vote(self):
        final_results = []
        results = []
        precisions = []
        cases_got_right = 0
        tree_index = 0
        for decision_tree in self.decision_tree_list:
            for case in self.validation_data:
                if 'Result' in case:
                    result = case.pop('Result')
                tree_result = decision_tree.classify(case)
                if tree_result == result:
                    cases_got_right += 1
                if len(results) <= tree_index:
                    results.append([tree_result])
                else:
                    results[tree_index] += [tree_result] 
            precisions.append(cases_got_right/len(self.validation_data))
            print("TREE " + str(tree_index) + " RESULT: " + str(results[tree_index]) + " PRECISION: " + str(precisions[tree_index]))
            tree_index += 1
            cases_got_right = 0
        for i in range(0, len(results[0])):
            dic = {}
            for j in range(0, len(results)):
                if results[j][i] not in dic:
                    dic[results[j][i]] = 1*precisions[j]
                else:
                    dic[results[j][i]] += 1*precisions[j]
            final_results.append(sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[0][0])
        return final_results