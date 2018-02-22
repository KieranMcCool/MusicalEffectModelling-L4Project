import dataloader as d
import numpy as np
from random import randrange

# Shorthand for the functions
ohe = lambda x : d.oneHotEncode(x)
ohd = lambda x : d.oneHotDecode(x)
lMap = lambda x,func : [func(e) for e in x]

# Allows you to generate new test data really easily
testData = lambda : np.array([ [randrange(-100, 100) for x in range(64)] for i in range(10) ])

"""
def oneHotBatchEncoder(batches):
    outputs = []
    for batch in batches:
        for sample in batch:
           outputs += [ohe(sample)] 
    return outputs

def oneHotBatchDecoder(batches):
    outputs = []
    for batch in batches:
        for sample in batch:
           outputs += [ohd(sample)] 
    return outputs
"""

def oneHotBatchEncoder(batches):
    outputs = []
    encoder = lambda x : ohe(x)
    mapper = np.vectorize(encoder)
    for batch in batches:
        for sample in batch:
           outputs += [mapper(sample)]
    return outputs

def oneHotBatchDecoder(batches):
    outputs = []
    encoder = lambda x : ohd(x)
    mapper = np.vectorize(encoder)
    for batch in batches:
        for sample in batch:
           outputs += [mapper(sample)]
    return outputs

