from scipy.io import wavfile as wf
from os import walk
import torch
import numpy as np
import globals

def loadWav(inputFile):
    _, data = wf.read(inputFile)
    return data

def writeWav(data, outputFile, sampleRate=globals.SAMPLE_RATE):
    wf.write(outputFile, sampleRate, data)

def padEnd(array, padding):
    pad = np.zeros(padding)
    return np.concatenate((array, pad))

def padStart(array, padding):
    pad = np.zeros(padding)
    return np.concatenate((pad, array))
