from globals import INPUT_VECTOR_SIZE, BATCH_SIZE
import torch
from dataloader import loadWav, padStart, padEnd
import numpy as np

def batchify(f):
    samplesVector = []
    targetsVector = []
    
    # f is [ [ sample1InputVector, sample1TargetVector ], ... ] 
    for s in f:
       samplesVector += [s[0]]
       targetsVector += [s[1]] 

    return [np.array(samplesVector), np.array(targetsVector)]

class WavFile:

    rawData = None
    processedData = []

    def __init__(self, data, procData=None):
        self.rawData = data
        if type(procData) is np.ndarray:
            self.processedData = procData
    
    # Returns an input vector and the target value in a list
    # Format : [ [List of Input Vectors], TargetValue ] 
    def getSample(self, i):

        TargetValue = self.processedData[i]
        # Pad data if it's before or after the end of the file.
        if i < 0 or i > len(self.rawData):
            return np.zeros(INPUT_VECTOR_SIZE)

        halfSize = INPUT_VECTOR_SIZE // 2
         
        firstHalf = self.rawData[i - halfSize if i - halfSize > 0 else 0:i]
        if len(firstHalf) < halfSize:
            firstHalf = padStart(firstHalf, halfSize - len(firstHalf)) 

        endIndex = i + 1 + halfSize
        endIndex = endIndex if endIndex < len(self.rawData) else len(self.rawData)
        secondHalf = self.rawData[i + 1:endIndex]

        if len(secondHalf) < halfSize:
            secondHalf = padEnd(secondHalf, halfSize - len(secondHalf))
        
        InputVector = np.concatenate((
            (firstHalf, secondHalf)))

        InputVector = np.array([ [element] for element in InputVector])

        return [InputVector, TargetValue]

    def __get_item__(self, key):
        return format(self, key) 
    def __set_item__(self, key, value):
        rawData[key] = value
    def len(self):
        return len(self.rawData)
