'''
Created on Mar 30, 2016

@author: dolphinigle
'''

import os.path
import parser

from engine import TestData
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

def Run(classifier_class, sample_folders, test_folders):
  print 'Preprocessing sample datas {0}...'.format(sample_folders)
  sample_datas = []
  for folder_name in sample_folders:
    normal_input = parser.ReadBAM(os.path.join(
        TESTDATA_FOLDER, folder_name, TUMOR_INPUT_FILENAME.format(folder_name)))
    tumor_input = parser.ReadBAM(os.path.join(
        TESTDATA_FOLDER, folder_name, NORMAL_INPUT_FILENAME.format(folder_name)))
    results = [parser.ReadVCF(os.path.join(TESTDATA_FOLDER, folder_name, vcf_filename.format(folder_name))) for vcf_filename in RESULT_FILENAMES]
    truth = parser.ReadBED(os.path.join(
        TESTDATA_FOLDER, folder_name, TRUTH_FILENAME.format(folder_name)))
    sample_datas.append(TestData(normal_input,
                                 tumor_input,
                                 results,
                                 truth))

  print 'Preprocessing test datas {0}...'.format(test_folders)
  test_datas = []
  for folder_name in test_folders:
    normal_input = parser.ReadBAM(os.path.join(
        TESTDATA_FOLDER, folder_name, TUMOR_INPUT_FILENAME.format(folder_name)))
    tumor_input = parser.ReadBAM(os.path.join(
        TESTDATA_FOLDER, folder_name, NORMAL_INPUT_FILENAME.format(folder_name)))
    results = [parser.ReadVCF(os.path.join(TESTDATA_FOLDER, folder_name, vcf_filename.format(folder_name))) for vcf_filename in RESULT_FILENAMES]
    #truth = None
    truth = parser.ReadBED(os.path.join(
        TESTDATA_FOLDER, folder_name, TRUTH_FILENAME.format(folder_name)))
    test_datas.append(TestData(normal_input,
                               tumor_input,
                               results,
                               truth))

  print 'Building {0} from {1}...'.format(classifier_class.__name__, sample_folders)
  classifier = classifier_class(test_datas)
  print 'Classifier constructed.'

  for test_data, test_folder in zip(test_datas, test_folders):
    print 'Running classifier on {0}'.format(test_folder)
    result = classifier.Classify(test_data)
    f1, precision, recall = eval_lib.Evaluate(test_data.bed, result)
    print 'F1 score: {0}'.format(f1)
    print 'Precision: {0}'.format(precision)
    print 'Recall: {0}'.format(recall)


if __name__ == '__main__':
  Run(engine.NaiveLearner, ['syn1'], ['syn1'])



