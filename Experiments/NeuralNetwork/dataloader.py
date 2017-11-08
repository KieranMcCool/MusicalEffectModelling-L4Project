from scipy.io import wavfile as wf
from os import walk
import torch
import numpy as np

SAMPLE_RATE = 44100
CHUNK_DURATION = 8

def loadWav(inputFile):
    _, data = wf.read(inputFile)
    return data

def writeWav(sampleRate, data, outputFile):
    wf.write(outputFile, sampleRate, data.numpy())

def pad(array, padding):
    return np.concatenate((array, np.zeros(padding)))

def chunk(data):
    chunkSize = SAMPLE_RATE * CHUNK_DURATION
    chunks = []
    if len(data) % chunkSize != 0:
        data = pad(data, len(data) % chunkSize)
    for i in range(0, len(data), chunkSize):
        chunks += [ data[i:i+chunkSize] ]
    return chunks

def getDatasets():

    # Format of data: [ [ fileA, fileAProcessed ], [fileB, FileBProcessed] ... ]

    getFiles = lambda x : ([ '%s/%s' % (x,  l) 
        for l in list(walk(x))[0][2] if l.endswith('.wav')])

    output = []

    raw = getFiles('./dataset')
    processed = getFiles('./dataset/processed')

    for i in range(len(raw)):
        rawChunks = chunk(loadWav(raw[i]))
        processedChunks = chunk(loadWav(processed[i]))
        output += [ [ rawChunks, processedChunks ] ]
    return output