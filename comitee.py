from decisiontree import decisiontree
from bayes import calculateBayes
import operator

class comitee:
    def __init__(self, decision_tree_list=None, validation_data=None):
        self.decision_tree_list = decision_tree_list
        self.validation_data = validation_data

    def copy_data(self):
        copy = []
        for item in self.validation_data:
            copy.append(item.copy())
        return copy 

    def classify_set_with_all_trees(self):
        results = []
        precisions = {}
        for i in range(0, len(self.decision_tree_list)):
            classified = self.classify_set(self.decision_tree_list[i], self.copy_data())
            for j in range(0, len(classified[0])):
                if j >= len(results):
                    results.append({i : classified[0][j]})
                else:
                    results[j][i] = classified[0][j]
            precisions[i] = classified[1]
        print("RESULTS: " + str(results) + " PRECISIONS: " + str(precisions))
        return (results, precisions)

    def classify_set(self, tree, dataset):
        result = ''
        results = []
        cases_got_right = 0
        for case in dataset:
            if 'Result' in case:
                result = case.pop('Result')
            tree_result = tree.classify(case)
            if tree_result == result:
                cases_got_right += 1
            results.append(tree_result)
        precision = (cases_got_right/float(len(dataset)))
        print("RESULT: " + str(results) + " PRECISION: " + str(precision))
        return (results, precision)

    def vote(self):
        final_results = []
        results_and_precisions = self.classify_set_with_all_trees()
        results = results_and_precisions[0]
        for i in range(0, len(results)):
            dic = {}
            for j in results[0].keys():
                if results[i][j] not in dic:
                    dic[results[i][j]] = 1
                else:
                    dic[results[i][j]] += 1
            final_results.append(sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[0][0])
        return final_results

    def weighted_vote(self):
        final_results = []
        results_and_precisions = self.classify_set_with_all_trees()
        results = results_and_precisions[0]
        precisions = results_and_precisions[1]
        for i in range(0, len(results)):
            dic = {}
            for j in results[0].keys():
                if results[i][j] not in dic:
                    dic[results[i][j]] = 1*precisions[j]
                else:
                    dic[results[i][j]] += 1*precisions[j]
            final_results.append(sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[0][0])
        return final_results

    def stacking(self):
        final_results = []
        results_and_precisions = self.classify_set_with_all_trees()
        results = results_and_precisions[0]
        for i in range(0, len(results)):
            results[i]['Result'] = self.validation_data[i]['Result']
        for case in results:
            final_results.append(calculateBayes(results, case))
        return final_results