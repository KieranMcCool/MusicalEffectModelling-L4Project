from globals import INPUT_VECTOR_SIZE
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
    # Format : [ [InputVector], TargetValue ] 
    def format(self, i):
        halfSize = INPUT_VECTOR_SIZE // 2
        
        firstHalf = self.rawData[i - halfSize if i - halfSize > 0 else 0:i]
        if len(firstHalf) < halfSize:
            firstHalf = padStart(firstHalf, halfSize - len(firstHalf)) 

        endIndex = i + 1 + halfSize
        endIndex = endIndex if endIndex < len(self.rawData) else len(self.rawData)
        secondHalf = self.rawData[i + 1:endIndex]

        if len(secondHalf) < halfSize:
            secondHalf = padEnd(secondHalf, halfSize - len(secondHalf))

        TargetValue = 0
        if len(self.processedData) != 0:
            TargetValue = self.processedData[i]
        
        InputVector = np.concatenate((firstHalf, secondHalf))
        return [InputVector, TargetValue]

    def __get_item__(self, key):
        return rawData[key]
    def __set_item__(self, key, value):
        rawData[key] = value
        
    def len(self):
        return len(self.rawData)
