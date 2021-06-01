#!/usr/bin/env python3
# Name: Rob Lodes (rlodes), Michael Farley (mf...)
# bme160 final project

import glob
from mitoUtils import SamReader


########################################################################
# Main
########################################################################

# def main(inCL=None):
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

    for file in files:
        mySam = SamReader(file)  # use this for debugging.
        print(mySam.fname)


    #
    #     for head, seq, in myFasta.readFasta():
    #         seq = seq.replace('.', '').replace('_', '').replace('-', '')    # clean up seq
    #         tRNA(head, seq)                                                 # instanciate a tRNA
    #     tRNA.tRNAlist.sort(key = lambda element:element.head)               # sort base on the header
    #     for current in tRNA.tRNAlist:                                       # traverse the tRNAlist
    #         # send unique messages to all objects
    #         current.findUniques()                                           # call findUniques
    #         # send essential messages to all objects
    #         current.findEssentials()                                        # call findEssentials
    #         current.findPosition()                                          # call findPosition
    #         print(current.head.replace(' ', ''))                            # clean up header, and print
    #         print(current.seq)                                              # print the seq
    #         for element in current.outputList:                              # travers the outputList
    #             print(element)                                              # print the element

if __name__ == "__main__":
    main()
    # main(inFile='testData.txt')   # use this for debugging

    # glob, read is file paths to a list, and then use that list to read in the files.