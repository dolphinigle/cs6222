'''
Created on Mar 30, 2016

@author: dolphinigle
'''
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

