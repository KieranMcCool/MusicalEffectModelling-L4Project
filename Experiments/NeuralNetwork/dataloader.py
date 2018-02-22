from os import walk
import audioread
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

def oneHotEncode(i, bits=globals.SAMPLE_BIT_DEPTH):
    bits = 2 ** bits
    topmost = bits // 2
    bottommost = -1 * (bits // 2)
    Map = lambda x : int(np.interp(x, [bottommost, topmost], [0, bits]))

    x = np.zeros(bits)
    x[Map(i)] = 1
    return x

def oneHotDecode(l, bits=globals.SAMPLE_BIT_DEPTH):
    bits = 2 ** bits
    topmost = bits // 2
    bottommost = -1 * (bits // 2)
    Map = lambda x : int(np.interp(x, [0, bits], [bottommost, topmost]))
    return Map(np.argmax(l))
