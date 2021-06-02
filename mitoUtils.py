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
        header = ''
        sequence = ''

        with self.doOpen() as samFile:
            reader = csv.reader(samFile, dialect='excel-tab')
            for row in reader:
                # print(row)
                pass
        #     header = ''
        #     sequence = ''
        #
        #     # skip to first fasta header
        #     line = fileH.readline()
        #     while not line.startswith('sam'):
        #         line = fileH.readline()
        #     header = line[1:].rstrip()
        #
        #     for line in fileH:
        #         if line.startswith('sam'):
        #             yield header, sequence
        #             header = line[1:].rstrip()
        #             sequence = ''
        #         else:
        #             sequence += ''.join(line.rstrip().split()).upper()
        #
        yield row

class mitoSet:
    fileSet = set()

    def __init__(self, file, row):
        self.file = file
        self.row = row
        self.fileList = {}

        self.fileList[file] = row


    def printRow(self):

        print(self.fileList.values())

# list of files, differenceSet