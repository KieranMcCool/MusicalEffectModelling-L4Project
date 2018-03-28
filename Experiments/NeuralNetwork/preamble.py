import dataloader as d
import numpy as np
from random import randrange

def one_hot_encode(data, channels=256):
    one_hot = np.zeros((data.size, channels), dtype=float)
    one_hot[np.arange(data.size), data.ravel()] = 1

    return one_hot


def one_hot_decode(data, axis=1):
    decoded = np.argmax(data, axis=axis)

    return decoded


def mu_law_encode(audio, quantization_channels=256):
    """
    Quantize waveform amplitudes.
    Reference: https://github.com/vincentherrmann/pytorch-wavenet/blob/master/audio_data.py
    """
    mu = float(quantization_channels - 1)
    quantize_space = np.linspace(-1, 1, quantization_channels)

    quantized = np.sign(audio) * np.log(1 + mu * np.abs(audio)) / np.log(mu + 1)
    quantized = np.digitize(quantized, quantize_space) - 1

    return quantized


def mu_law_decode(output, quantization_channels=256):
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

def encode(x):
    return one_hot_encode(mu_law_encode(x))

def decode(x):
    return mu_law_decode(one_hot_decode(x))

