#!/usr/bin/env python

import numpy as np
from sys import argv
from scipy.signal import chirp, sawtooth, square
from scipy.io import wavfile as wf
from random import randrange, uniform

low = 80
high = 1200
duration = 10
sampleRate = 44100
reaperLocation = '/Applications/REAPER64.app/Contents/MacOS/REAPER'

def sliceAudio(input, destination, index):
    # Insert note slice into output at random location,
    # ensure input fits into destination from index.
    destination[index:index+len(input)] += input
    return destination

def sinewave(f, duration=duration):
    # single note
    return (np.sin(2 * np.pi * 
        np.arange(sampleRate*duration)
        * f/sampleRate))

def sweep(low=low, high=high, duration=duration):
    # useful for sweeping frequency ranges of instruments
    space = np.linspace(0, 10, duration * sampleRate)
    return chirp(space, low, 10, high)

def sawtooth(f, duration=duration):
    # Generates clicks at low f values
    space = np.linspace(0, 10, duration * sampleRate)
    return square(2 * np.pi * f * space)

def noteChanges():

    # Complexity (Number of notes):
    # 40% chance of 5 to 50, 40% chance of 1 to 10, 10% chance of 10 to 100,
    # 10% chance of 100 to 150
    complexity = randrange(0, 100)
    notes = (randrange(5,   50)   if complexity < 40
        else randrange(1,   10)   if complexity < 80
        else randrange(10,  100)  if complexity < 90
        else randrange(100, 150))

    output = np.zeros(duration*sampleRate)

    for n in range(notes):

        # Note Duration:
        # 30% chance of 1 second, 30% chance of 1 to 3 seconds, 
        # 20% chance of 0 to 1 second, 20% chance of 0 to 0.5 seconds
        noteDuration = randrange(0, 100)
        d = (    1        if noteDuration < 30
            else randrange(1, 3) if noteDuration < 60
            else uniform(0, 1)   if noteDuration < 80
            else uniform(0, 0.5))

        # Frequency Choices
        f1 = low
        f2 = high # only required for sweep
        
        # Note Type:
        # 40% chance of sine, 40% chance of a sawtooth, 
        # 20% chance of a chirp
        noteType = randrange(0, 100)
        note = (sinewave(f1,  duration = d) if noteType < 40
            else sawtooth(f1, duration = d) if noteType < 80
            else sweep(low = f1, high=  f2, duration = d))

        # Append to output
        sliceAudio(note, output, randrange(0, len(output) - len(note)))

    return output

def output(filename, data):
    wf.write(filename, sampleRate, data)

def generate(files, sections):
    for f in range(files):
        sectionDuration = duration * sampleRate
        data = np.zeros(sectionDuration * sections)

        for s in range(sections):
            startIndex = sectionDuration * s
            endIndex = startIndex + sectionDuration
            data[startIndex:endIndex] = noteChanges()
        output("dataset/%s.wav" % f, data)

def main():
    files = 1
    sections = 1
    try:
        if '-n' in argv:
            files = int(argv[argv.index('-n') + 1])
        if '-s' in argv:
            sections = int(argv[argv.index('-s') + 1])
    except:
        print("Usage: ./main.py [-n number] [-s number]\n",
            "\tIf no arguments are given, it generates one random wav file.")

    generate(files, sections)
    
if __name__ == '__main__':
    main()
