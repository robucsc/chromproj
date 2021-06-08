#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mijfarle)
# PI: Miten Jain
# bme160 final project


import sys
import csv

class SamReader:
    '''
    '''

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
        rowList = []
        rowList.append(row[2])
        self.mitoDict[row[1]] = rowList                     # add reference base
        self.addRow(row)

    def addRow(self, row):
        try:
            base = self.baseDict[row.index('1', 13, 21)]    # interest, start, end
            self.mitoDict[row[1]].append(base)
        except:
            # print('failure is not an option')
            pass
        # print(self.mitoDict[row[1]])

    def differencePosition(self):
        diffPos = []
        for key in self.mitoDict:
            if(len(set(self.mitoDict[key]))) != 1:
                diffPos.append(key)
        # for value in self.mitoDict:
        #     pass
        print(diffPos)

