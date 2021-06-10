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
    Input: pysam files in the data subdirectory
    Output: fasta file with seqs of interest to STDOUT
    Example use: python mito.py
    '''

    # Returns a list of names in list files.
    files = glob.glob('./data/*.txt', recursive = True)
    myMito = mitoDictionary()

    mySam = SamReader(files[0])     # input the first file
    for row in mySam.readSam():
        myMito.addPrimeRow(row)

    for file in range(1, len(files)):    # input from second file on
        mySam = SamReader(files[file])
        for row in mySam.readSam():
            myMito.addRow(row)

    distance = 10       # number of bases to each side of the point of interest

    for index in range(0, len(files)):
        myMito.outputFasta(files[index], distance, index)

    
if __name__ == "__main__":
    main()


