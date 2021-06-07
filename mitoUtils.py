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
            reader = csv.reader(samFile, dialect='excel-tab')
            skipHeader = next(reader)
            for row in reader:
                yield row

class mitoDictionary:
    fileSet = {}

    def __init__(self):
        # self.fileList = []
        self.diffList = []
        self.mito = {}
        self.baseDict = {13: 'A', 15: 'C', 17: 'T', 19: 'G', 21: 'N'}

    def addPrimeRow(self, row):
        # self.mito[row[1]].update(self.mito[row[2]])         # add reference base
        # self.mito({row[1]:row[2]})
        self.mito[row[1]] = row[2]
        
        self.addRow(row)

    def addRow(self, row):
        if (row[5] !=  1):
            base = self.baseDict.get(row.index('1', 13, 21))  # interest, start, end
            # self.mito[row[1]].append(self.mito[row[base]])
            self.mito[row[1]] = base



    # def printStandRow(self):
    #     print(self.standList)

    # def printRow(self):
    #     print(self.fileList)

    # def compareFile(self):
    #     # print(self.fileList.keys())
    #     # print(self.fileList.values())
    #     for file in self.fileList:
    #         self.diffList = self.standList or file
    #         print(self.diffList)
    #         # pass
            
            

        # nuList = list(self.fileList.keys())
        # print(nuList)
        # for current in nuList:
            # print("in loop")
            # print(current)

        # self.fileList.values().

# list of files, differenceSet
#
# dictionary-->set-->list
#
# difference-->build seq-->list
#
# dictonary list of files
#     each file set of stirngs
#
# file 0 set of stirgs compared to file 2 set of strigs
#  from 1 to 4
#     compare current to standard
#
#
# set 1 or set 2


# line.strip().split('\t')


