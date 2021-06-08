#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mijfarle)
# PI: Miten Jain
# bme160 final project


import sys
import csv

class SamReader:
    '''
    '''

    # csv.reader(fileName, dialect = 'excel-tab')

    def __init__(self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname

    def doOpen(self):
        ''' Handle file opens, allowing STDIN.'''
        if self.fname == '':
            return sys.stdin
        else:
            return open(self.fname)

    def readSam(self):
        ''' Read an entire sam file and return one row at a time till EOF'''
        with self.doOpen() as samFile:
            reader = csv.reader(samFile, dialect='excel-tab') # reads data into a list
            next(reader)   # using next to skip the file header
            for row in reader:
                yield row

class mitoDictionary:

    def __init__(self):
        self.mitoDict = {}
        self.baseDict = {13: 'A', 15: 'C', 17: 'T', 19: 'G', 21: 'N'}

    def addPrimeRow(self, row):
        # self.mitoDict[row[1]].update(self.mitoDict[row[2]])         # add reference base
        # self.mitoDict({row[1]:row[2]})
        self.mitoDict[row[1]] = row[2]
        self.addRow(row)

    def addRow(self, row):
        if (row[5] !=  1):
            base = self.baseDict.get(row.index(1, 13, 21))  # interest, start, end
            # self.mitoDict[row[1]].append(self.mitoDict[row[base]])
            self.mitoDict[row[1]] = base

