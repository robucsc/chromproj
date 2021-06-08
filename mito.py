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
    # print("Using glob.glob()")
    files = glob.glob('./data/*.txt', recursive = True)
    myMito = mitoDictionary()

    mySam = SamReader(files[0])     # process the first file
    # print(files[0])
    for row in mySam.readSam():
        myMito.addPrimeRow(row)

    for i in range(1,len(files)):    # from second file on
        mySam = SamReader(files[i])  # use this for debugging.
        for row in mySam.readSam():
            myMito.addRow(row)

    
if __name__ == "__main__":
    main()


