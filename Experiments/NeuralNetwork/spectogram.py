import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from sys import argv as args

isMain = False

def spectogram(f):
    global isMain
    # Load sound file
    y, sr = librosa.load(f)

    # Let's make and display a mel-scaled power (energy-squared) spectrogram
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

    # Convert to log scale (dB). We'll use the peak power as reference.
    log_S = librosa.logamplitude(S, ref_power=np.max)

    # Make a new figure
    plt.figure(figsize=(20,4))

    # Display the spectrogram on a mel scale
    # sample rate and hop length parameters are used to render the time axis
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

    # Put a descriptive title on the plot
    plt.title(f)

    # draw a color bar
    plt.colorbar(format='%+02.0f dB')

    # Make the figure layout compact
    plt.tight_layout()
    if isMain:
        plt.show()
    else:
        plt.savefig(f + '.png')

def main():
    f = args[1]
    spectogram(f)

if __name__ == '__main__':
    isMain = True
    main()
