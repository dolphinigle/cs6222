'''
Created on Mar 30, 2016

@author: dolphinigle
'''

from pysam import AlignmentFile
from pysam import VariantFile

import models


# Note that the chromosomes here do not use 'chr'. Instead of 'chr14' they are just '14'.
def ReadBAM(filename):
  # Read from given BAMFile. Returns an iterable, each is an interesting object.
  bamfile = AlignmentFile(filename, 'rb')
  return bamfile


def ReadVCF(filename):
  # Same with ReadBAM
  # NOTE: the file is missing a header, and must be manually added.
  vcf_file = VariantFile(filename)
  return vcf_file


def ReadBED(filename):
  bed_file = open(filename)
  snvs = []
  for line in bed_file:
    chromosome, start, stop = line.rstrip().split()
    snvs.append(models.SNV(chromosome, start, stop))
  return snvs


