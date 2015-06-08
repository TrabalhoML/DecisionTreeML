from random_forest import split_dataset
from decisiontree import decisiontree
from comitee import comitee
import random
def cross_validation(dataset,splits=10,include_whole_tree=False,forest_size=3):


    random.shuffle(dataset)
    step = len(dataset)//splits
    results_votes = 0
    results_wvotes = 0
    results_stacking = 0

    for i in range(10):
        training = dataset[:i*step] + dataset[(i+1)*step:]
        test = dataset[i*step:(i+1)*step]
        forest = split_dataset(training,forest_size)
        if include_whole_tree:
            forest.append(decisiontree(training_data=training))
        comitee_t = comitee(forest,test)
        results_votes += comitee_t.calculate_precision(comitee_t.vote())
        results_wvotes += comitee_t.calculate_precision(comitee_t.weighted_vote())
        results_stacking += comitee_t.calculate_precision(comitee_t.stacking())

        
    return (results_votes/10,results_wvotes/10,results_stacking/10)
