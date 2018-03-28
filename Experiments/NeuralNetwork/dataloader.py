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

Channels = 2**16

def one_hot_encode(data, channels=Channels):
    one_hot = np.zeros((data.size, channels), dtype=float)
    one_hot[np.arange(data.size), data.ravel()] = 1

    return one_hot

def one_hot_decode(data, axis=1):
    decoded = np.argmax(data, axis=axis)

    return decoded

def mu_law_encode(audio, quantization_channels=Channels):
    """
    Quantize waveform amplitudes.
    Reference: https://github.com/vincentherrmann/pytorch-wavenet/blob/master/audio_data.py
    """
    mu = float(quantization_channels - 1)
    quantize_space = np.linspace(-1, 1, quantization_channels)

    quantized = np.sign(audio) * np.log(1 + mu * np.abs(audio)) / np.log(mu + 1)
    quantized = np.digitize(quantized, quantize_space) - 1

    return quantized.astype(int)

def mu_law_decode(output, quantization_channels=Channels):
    """
    Recovers waveform from quantized values.
    Reference: https://github.com/vincentherrmann/pytorch-wavenet/blob/master/audio_data.py
    """
    mu = float(quantization_channels - 1)

    expanded = (output / quantization_channels) * 2. - 1
    waveform = np.sign(expanded) * (
                   np.exp(np.abs(expanded) * np.log(mu + 1)) - 1
               ) / mu

    return waveform
