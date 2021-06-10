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
        self.diffPos = []

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

    def differencePosition(self):
        for key in self.mitoDict:
            if(len(set(self.mitoDict[key]))) != 1:
                self.diffPos.append(key)
    
    def findFullSeq(self):
        seq = ''
        for key in self.mitoDict:
            seq = seq + self.mitoDict[key][0]
        return (seq)

    def findSeq(self, position, distance, index):
        seq = ''
        if (position > distance):
            start = position - distance
        else:
            start = distance - position
        stop = position + distance
        try:
            for key in range(start, stop):
                seq = seq + self.mitoDict[str(key)][index + 1]
        except:
            # print('failure is not an option')
            pass

        return (seq)
        
    def outputFasta(self, file, distance, index):
        self.differencePosition()
        fileName = file.split('/')[-1]
        for diff in self.diffPos:
            print('>', 'file', fileName, 'position', diff,
                  ';chrM-', int(diff) - distance, '-', int(diff) + distance + 1)
            print(self.findSeq(int(diff), distance, index))

