'''
Created on Mar 30, 2016

@author: dolphinigle
'''
from collections import namedtuple

from sklearn import tree

from constants import RESULT_FILENAMES
import constants
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
    # test_datas is a list of TestData
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


class Point(object):
  def __init__(self,
               chromosome,
               ):
    if chromosome == 'X':
      chromosome = '23'
    elif chromosome == 'Y':
      chromosome = '24'
    self.chromosome = int(chromosome)
    self.results = [0] * len(RESULT_FILENAMES)

  def Arrayize(self):
    return self.results
    return [self.chromosome] + self.results

  @staticmethod
  def FeatureNames():
    return constants.RESULT_FILENAMES
    return ['Chromosome',] + constants.RESULT_FILENAMES


def TestDataToPoints(test_data):
  raw_points = {}
  for i, vcf in enumerate(test_data.vcfs):
    for p in vcf:
      pos = p.pos
      chromosome = p.chrom
      iden = (chromosome, pos)
      if iden not in raw_points:
        raw_points[iden] = Point(chromosome)
      raw_points[iden].results[i] = 1
  return raw_points


class DecisionTreeLearner(object):
  def __init__(self, test_datas):
    points = []
    results = []
    for test_data in test_datas:
      raw_points = {}

      truths = set()

      for truth in test_data.bed:
        iden = (truth.chromosome, truth.start)
        raw_points[iden] = Point(truth.chromosome)
        truths.add(iden)

      for iden, point in TestDataToPoints(test_data).items():
        raw_points[iden] = point

      for iden, point in raw_points.items():
        points.append(point)
        if iden in truths:
          results.append(1)
        else:
          results.append(0)

    sample_array = []
    for point in points:
      sample_array.append(point.Arrayize())
    decision_tree = tree.DecisionTreeClassifier()
    decision_tree = decision_tree.fit(sample_array, results)
    self.decision_tree = decision_tree

    tree.export_graphviz(decision_tree,
        out_file='imgs/decision_tree.dot',
        feature_names=Point.FeatureNames()) 


  def Classify(self, test_data):
    # Return SNVs
    raw_points = TestDataToPoints(test_data)
    points = []
    idens = []
    for iden, point in raw_points.items():
      points.append(point.Arrayize())
      idens.append(iden)
    results = self.decision_tree.predict(points)
    snvs = []
    for iden, result in zip(idens, results):
      assert result in [0, 1]
      if result:
        snvs.append(models.SNV(iden[0], iden[1], iden[1]))
    return snvs


