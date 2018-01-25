from globals import INPUT_VECTOR_SIZE, BATCH_SIZE, SAMPLE_RATE
import torch
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.sampler import RandomSampler, SequentialSampler, Sampler
from dataloader import loadWav, padStart, padEnd
import numpy as np
from random import shuffle

class LazyDataset(Dataset):

    def __init__(self, data, procData=None):
        super(LazyDataset, self).__init__()
        self.rawData = data
        if type(procData) is np.ndarray:
            self.processedData = procData
    
    # Returns an input vector and the target value in a list
    # Format : [ [List of Input Vectors], TargetValue ] 
    def __getitem__(self, i):

        InputVector = None
        TargetValue = torch.Tensor([[self.processedData[i]]])
        if INPUT_VECTOR_SIZE == 1:
            InputVector = torch.Tensor([[self.rawData[i]]])
        else:
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

            InputVector = torch.Tensor([[element for element in InputVector]])

        return [InputVector, TargetValue]

    def __len__(self):
        return len(self.rawData)

    def randomSampler(self):
        return DataLoader(self, batch_size=BATCH_SIZE, 
                sampler=RandomSampler(self),
                num_workers=4)

    def sequentialSampler(self):
        return DataLoader(self, batch_size=BATCH_SIZE, 
                sampler=SequentialSampler(self),
                num_workers=4)

    def randomSequentialSampler(self):
        return DataLoader(self, batch_size=BATCH_SIZE, 
                # 5 Seconds (SAMPLE_RATE * 5) seems a reasonable enough time.
                sampler=RandomSequentialSampler(self, SAMPLE_RATE * 5),
                num_workers=4)

class RandomSequentialSampler(Sampler):
    def __init__(self, datasource, seqCount):
        self.source = datasource
        self.seqCount = seqCount

    def __iter__(self):
        flatten = lambda l: [item for sublist in l for item in sublist]
        groups = [[range(i, i + self.seqCount)] for i in range(0,len(self),self.seqCount)]
        shuffle(groups)
        groups = flatten(flatten(groups))
        return iter(groups) 

    def __len__(self):
        return len(self.source)


