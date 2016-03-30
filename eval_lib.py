'''
Created on Mar 30, 2016

@author: dolphinigle
'''

def Evaluate(truth_snvs, result_snvs):
  # Returns (f1, precision, recall)
  truth_set = set(truth_snvs)
  result_set = set(result_snvs)
  intersection = truth_set.intersection(result_set)
  print len(truth_set), len(result_set)
  assert len(truth_set)
  assert len(result_set)
  precision = 1.0 * len(intersection) / len(truth_set)
  recall = 1.0 * len(intersection) / len(result_set)
  if (precision + recall):
    f1 = 2 * precision * recall / (precision + recall)
  else:
    f1 = 0
  return (f1, precision, recall)

