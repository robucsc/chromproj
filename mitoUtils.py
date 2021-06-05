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
        ''' Read an entire FastA record and return the sequence header/sequence'''

        with self.doOpen() as samFile:
            reader = csv.reader(samFile, dialect='excel-tab')
            for row in reader:
                # print(row)

                yield '-'.join(row) # join to work in a set

class mitoSet:
    fileSet = set()

    def __init__(self):
        self.fileList = []
        self.standList =[]
        self.diffList = []
        # self.fileList = {}

        # self.fileList[file] = row
        
    def addStand(self, file):
        self.standList.append(file)

    def addFile(self, file):
        self.fileList.append(file)

    def addRow(self, file, row):
        makeSet = set([])
        makeSet = row
        self.fileList.append(makeSet)

    def printStandRow(self):
        print(self.standList)

    def printRow(self):
        print(self.fileList)

    def compareFile(self):
        # print(self.fileList.keys())
        # print(self.fileList.values())
        for file in self.fileList:
            self.diffList = self.standList or file
            # print(self.diffList)
            
            

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


