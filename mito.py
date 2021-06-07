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

    mySam = SamReader(files[0])
    for row in mySam.readSam():
        myMito.addPrimeRow(row)
            
    for file in range(1,len(files)):    # from second file on
        mySam = SamReader(file)  # use this for debugging.
        # print(mySam.fname)
        mySam.readSam()
        # next(mySam.readSam) # skip header
        for row in mySam.readSam():
            myMito.addRow(row)

        # myMito.compareFile()
    # myMito.printRow()
    
if __name__ == "__main__":
    main()
    # main(inFile='testData.txt')   # use this for debugging

