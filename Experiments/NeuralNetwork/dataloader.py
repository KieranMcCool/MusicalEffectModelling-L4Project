from os import walk
from librosa.core import load
from librosa.output import write_wav
import torch
import numpy as np
import globals

def loadWav(inputFile):
    data = load(inputFile, sr=globals.SAMPLE_RATE, mono=True, dtype=float)[0]
    return data

def writeWav(data, outputFile, sampleRate=globals.SAMPLE_RATE):
    write_wav(outputFile, data, sampleRate)

def padEnd(array, padding):
    pad = np.zeros(padding)
    return np.concatenate((array, pad))

def padStart(array, padding):
    pad = np.zeros(padding)
    return np.concatenate((pad, array))
