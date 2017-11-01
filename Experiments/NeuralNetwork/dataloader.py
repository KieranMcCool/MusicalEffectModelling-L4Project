from scipy.io import wavfile as wf
import torch

SAMPLE_RATE = 44100
CHUNK_DURATION = 8
CHUNK_SIZE = SAMPLE_RATE / CHUNK_DURATION

def loadWav(inputFile):
    _, data = wf.read(inputFile)
    tensor = torch.from_numpy(data)
    return tensor

def writeWav(sampleRate, data, outputFile):
    wf.write(outputFile, sampleRate, data.numpy())

def pad(array):
    output = []
    lenghtDif = CHUNK_SIZE - len(array)
    if lenghtDif > 0:
        output = array + ([0] * lenghtDif)
    return output

def chunk(data):
    return None
