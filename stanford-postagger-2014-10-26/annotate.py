#!/usr/bin/env python
#The above line specifies to the Unix that the file is a python script 

"""
COMPUTATIONAL LINGUISTICS

PYTHON TIPS AND TRICKS (Sep 17, 2014)
"""

from __future__ import division          #integer division
from collections import defaultdict
import random
import string        #some string-related utilities
import sys        #for command-line args
import re    #for regular expressions
import os
import subprocess

#Metadata of your program
___author__ = 'Sravana Reddy'
__date__ = 'Sep 2014'
__version__ = '1'

#tag texts.txt files for each product ID with part-of-speeches
def annotate_pos(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            pathName = os.path.join(subdir, file)
            #for each texts.txt file in the data directory, call the stanford-part-of-speech tagger program
            #to annotate texts.txt with part-of-speeches, and store the annotations in a pos.txt file
            if pathName.endswith('texts.txt'):
                if not os.path.exists(os.path.join(subdir, 'pos.txt')):
                    subprocess.call(['./stanford-postagger.sh', './models/english-bidirectional-distsim.tagger', pathName], stdout=open(os.path.join(subdir, 'pos.txt'), 'w'))
    

#NOTE: must be in the stanford-postagger-2014-10-26 folder to call this program
if __name__=='__main__':   #main function
    annotate_pos('../data')