from globals import INPUT_VECTOR_SIZE, BATCH_SIZE
import torch
from dataloader import loadWav, padStart, padEnd
import numpy as np

class WavFile:

    rawData = None
    processedData = []

    def __init__(self, path, processedPath=None):
        self.rawData = loadWav(path)
        if processedPath != None:
            print('Loading Processed data...')
            self.processedData = loadWav(processedPath)
    
    # Returns an input vector and the target value in a list
    # Format : [ [List of Input Vectors], TargetValue ] 
    def format(self, i):
        def getVals(i):

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
            return InputVector
#            return np.array(InputVector, dtype=np.float) # returns array of 64x1

        # Calculate target value if we're training.
        TargetValue = 0
        if len(self.processedData) != 0:
            TargetValue = self.processedData[i]

        # Get batch size of input vectors either side of the target value.
        halfBatch = BATCH_SIZE // 2
#        Inputs = np.array([np.array([getVals(j) for j in range(i-halfBatch, i+halfBatch)])])
        return [np.array([getVals(i)]), TargetValue]

    def __get_item__(self, key):
        return format(self, key) 
    def __set_item__(self, key, value):
        rawData[key] = value
    def len(self):
        return len(self.rawData)
