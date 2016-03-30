'''
Created on Mar 30, 2016

@author: dolphinigle
'''

import os.path
import parser

import engine
import eval_lib


RESULT_FILENAMES = ['{0}_freebayes.vcf',
                    '{0}_mutect.vcf',
                    '{0}_vardict.vcf',
                    '{0}_varscan.vcf']

TRUTH_FILENAME = '{0}_truth.bed'

NORMAL_INPUT_FILENAME = '{0}_normal.bam'
TUMOR_INPUT_FILENAME = '{0}_tumor.bam'
TESTDATA_FOLDER = 'testdata'

def Run(method, folder_name):
  tumor_input = parser.ReadBAM(os.path.join(
      TESTDATA_FOLDER, folder_name, NORMAL_INPUT_FILENAME.format(folder_name)))
  normal_input = parser.ReadBAM(os.path.join(
      TESTDATA_FOLDER, folder_name, TUMOR_INPUT_FILENAME.format(folder_name)))
  truth = parser.ReadBED(os.path.join(
      TESTDATA_FOLDER, folder_name, TRUTH_FILENAME.format(folder_name)))
  results = [parser.ReadVCF(os.path.join(TESTDATA_FOLDER, folder_name, vcf_filename.format(folder_name))) for vcf_filename in RESULT_FILENAMES]
  print 'Running {0} on {1}...'.format(method.func_name, folder_name)
  run_result = method(normal_input, tumor_input, results)
  print 'Run completed.'
  f1, precision, recall = eval_lib.Evaluate(truth, run_result)
  print 'F1 score: {0}'.format(f1)
  print 'Precision: {0}'.format(precision)
  print 'Recall: {0}'.format(recall)
  return f1, precision, recall

if __name__ == '__main__':
  Run(engine.TestCombineResults, 'syn1')



