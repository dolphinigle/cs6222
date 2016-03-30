'''
Created on Mar 30, 2016

@author: dolphinigle
'''
from collections import namedtuple

import models


def TestCombineResults(normal_reads, tumor_reads, in_snvs):
  # Returns a list of SNVs.
  vcfs = in_snvs[0]
  snvs = []
  for anomaly in vcfs:
    snvs.append(models.SNV(anomaly.chrom,
                           anomaly.pos,
                           anomaly.pos))
  return snvs


TestData = namedtuple('TestData', ['normal_read',
                                   'tumor_read',
                                   'vcfs',
                                   'bed'])
# Additionally, it may have .bed: truth value from the input and .actual: truth calculated by classifier.


class Learner(object):
  def __init__(self, test_datas):
    # learn datas is a list of TestData
    pass

  def Classify(self, test_data):
    # Return result for this test data.
    pass


class NaiveLearner(object):
  def __init__(self, test_datas):
    # learn datas is a list of TestData
    pass

  def Classify(self, test_data):
    vcfs = test_data.vcfs[0]
    snvs = []
    for anomaly in vcfs:
      snvs.append(models.SNV(anomaly.chrom,
                             anomaly.pos,
                             anomaly.pos))
    return snvs


class DecisionTreeLearner(object):
  def __init__(self, test_datas):
    # learn datas is a list of TestData
    pass

  def Classify(self, test_data):
    # fill in the "bed" value in given test_data.
    pass


