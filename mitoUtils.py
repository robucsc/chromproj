#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mijfarle)
# PI: Miten Jain
# bme160 final project
'''

mitoUtils.py

This is a group of utilities for processing sam files.

Utilities: SamReader, MitoDictionary

'''
import sys
import csv

class SamReader:
    '''
    reads in  a sam-formatted file containing a tab delimited fields, and returns a series of lists
    Input: a sam file
    Output: a series of lists containing the fields from each row of the sam file
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
        ''' Read an entire sam file one row at a time till EOF '''
        with self.doOpen() as samFile:
            reader = csv.reader(samFile, dialect='excel-tab') # reads data into a list
            next(reader)   # using next to skip the file header
            for row in reader:
                yield row

class MitoDictionary:
    '''
        Analyzes a series of lists identifying points of interest, and extracts a sequence for each
            point of interest.
        Input: a series of lists
        Output: formatted output listing the seq name, and for each seq its POI, start and stop
            in the header, followed by the seq in the form af a fasta file.
        Methods: __init__, addPrimeRow, addRow, revComp, differencePosition, findFullSeq, findSeq,
            outputFasta
    '''
    def __init__(self):
        ''' init, bring in the arguments when called '''
        self.mitoDict = {}                                              # store base information
        self.baseDict = {13: 'A', 15: 'C', 17: 'T', 19: 'G', 21: 'N'}   # convert from col to base
        self.diffPos = []                                               # list of difference positions

    def addPrimeRow(self, row):
        ''' adds a row from the prime file to the dictionary '''
        rowList = []                                        # a list to hold the current row
        rowList.append(row[2])                              # add row info to the list
        self.mitoDict[row[1]] = rowList                     # add reference base
        self.addRow(row)

    def addRow(self, row):
        ''' adds a row from the non-prime files to the dictionary '''
        try:
            base = self.baseDict[row.index('1', 13, 21)]    # interest, start, end
            self.mitoDict[row[1]].append(base)              # add base to the dictionary
        except:
            # print('failure is not an option')
            pass

    def differencePosition(self):
        ''' finds the points of interest '''
        for key in self.mitoDict:                           # traverse the dictionary
            if(len(set(self.mitoDict[key]))) != 1:          # if length is not 1 then this is a POI
                self.diffPos.append(key)                    # add position as a POI
    
    def findFullSeq(self):
        ''' assembles the full reference sequence '''
        seq = ''
        for key in self.mitoDict:
            seq = seq + self.mitoDict[key][0]
        return (seq)

    def findSeq(self, position, distance, index):
        ''' assembles the reference seq for the POI for the requested file '''
        seq = ''
        if (position > distance):                                   # calculate start
            start = position - distance
        else:
            start = distance - position
        stop = position + distance                                  # calculate stop
        try:
            for key in range(start, stop):
                seq = seq + self.mitoDict[str(key)][index + 1]      # add base to seq
        except:
            # print('failure is not an option')
            pass
        return (seq)
        
    def outputFasta(self, file, distance, index):   # organize by file name
        ''' creates the output in the fasta format '''
        self.differencePosition()                                   # find POI
        fileName = file.split('/')[-1]                              # get file name for header, strip path
        for diff in self.diffPos:                                   # assemble header and seq, output fasta format
            print('> file ' + fileName + ' position ' + diff +
                  '; chrM-' + str(int(diff) - distance) + '-' + str(int(diff) + distance + 1))
            print(self.findSeq(int(diff), distance, index))

    def outputFastaPOI(self, files, distance):   # organize by POI
        ''' creates the output in the fasta format '''
        self.differencePosition()                                   # find POI
        for diff in self.diffPos:                                   # assemble header and seq, output fasta format
            for index in range(0, len(files)):                      # call the output method for each file name
                fileName = files[index].split('/')[-1]              # get file name for header, strip path
                print('> file ' + fileName + ' position ' + diff +
                  '; chrM-' + str(int(diff) - distance) + '-' + str(int(diff) + distance + 1))
                print(self.findSeq(int(diff), distance, index))