#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mijfarle)
# PI: Miten Jain
# bme160 final project

import glob
from mitoUtils import SamReader, mitoSet


########################################################################
# Main
########################################################################

def main(inFile=None):
    '''
    The Main function.
    Input: FastA sequences from STDIN
    Output: a list of essential substrings graphically positioned in relation to their position in the sequence
    Example use: python findUnique.py < dataFile.fa > output.txt
    '''

    # Returns a list of names in list files.
    print("Using glob.glob()")
    files = glob.glob('./data/*.txt', recursive = True)

    myMito = mitoSet()
    
    standFile = 'chm13.draft_v1.0.chrM.fa.chrm.sorted.bam.pysamstats.txt'
    standSam = SamReader(standFile) 
    standSam.readSam()
    myMito.addStand(standFile)
    for row in standSam.readSam():
        myMito.addRow(standFile, row)
    myMito.printStandRow()
        
        
    for file in files:
        mySam = SamReader(file)  # use this for debugging.
        # print(mySam.fname)
        mySam.readSam()
        myMito.addFile(file)

        for row in mySam.readSam():
            # print(row)
            myMito.addRow(file, row)

        myMito.compareFile()
    myMito.printRow()
    
if __name__ == "__main__":
    main()
    # main(inFile='testData.txt')   # use this for debugging

    # glob, read is file paths to a list, and then use that list to read in the files.