#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mijfarle)
# PI: Miten Jain
# bme160 final project

import glob
from mitoUtils import SamReader, mitoDictionary

########################################################################
# Main
########################################################################

def main(inFile=None):
    '''
    The Main function.
    Input:
    Output:
    Example use: python mito.py
    '''

    # Returns a list of names in list files.
    print("Using glob.glob()")
    files = glob.glob('./data/*.txt', recursive = True)
    myMito = mitoDictionary()
    
    for file in files:
        mySam = SamReader(file)  # use this for debugging.
        print(mySam.fname)
        mySam.readSam()
        myMito.addFile(file)
        # next(mySam.readSam) # skip header
        for row in mySam.readSam():
            # print(row)
            myMito.addRow(file, row)

        # myMito.compareFile()
    # myMito.printRow()
    
if __name__ == "__main__":
    main()
    # main(inFile='testData.txt')   # use this for debugging

