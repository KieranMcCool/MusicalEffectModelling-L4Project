import numpy as np
from dataloader import loadWav
from os import walk
from data import WavFile, batchify

def randomSampler(data):
    return 0

def sequentialSampler(data):
    return 0

def runTest():
    return 0

def main():
    def loadData():
        getFiles = lambda x : ([ '%s/%s' % (x,  l) 
            for l in list(walk(x))[0][2] if l.endswith('.wav')])

        dryFiles = getFiles('./dataset')
        wetFiles = getFiles('./dataset/processed')

        dryData = []
        wetData =  []
        # Iterate over files and processed files
        for file, pFile in zip(dryFiles, wetFiles):
           dryData = dryData  + list(loadWav(file))
           wetData = wetData + list(loadWav(pFile))
        return WavFile(np.array(dryData), np.array(wetData))

    loadData()
main()
