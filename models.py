'''
Created on Mar 30, 2016

@author: dolphinigle
'''

from collections import namedtuple

SNVBase = namedtuple('SNVBase', ['chromosome', 'start', 'stop'])

class SNV(SNVBase):
  def __new__(cls, chromosome, start, stop):
    assert start == stop
    return SNVBase.__new__(cls, chromosome, int(start), int(stop))

