% Minutes from Meeting 16
% Kieran McCool
% 15 Feb 2018

# Progress since last meeting

* Had some bugs appear
    - LibRosa started reporting that ffmpeg was missing despite being installed.
    - Turned out to be corrupted input data which is strange as it's never happened before...
    - Misplaced square bracket inside list comprehension was making the output of the network invalid as a wav file.
* Started final choice of VSTs/Effects and grouping
    - TS808 from Mercurial, ran some models to get evaluation data.
    - Voxengo Fuzz: didn't manage to get a decent model of this, needs more work
    - Thinking of trying Amp sims, couldn't find any good ones for VST, might use GarageBand. Downside is that I can't automate this process.
* WaveNet: Trying to implement WaveNet like network in PyTorch.
    - Some confusion...

# Questions

* WaveNet: How does input/output work
    - Example shows 256 size vector in, 256 size vector out.
    - Does this mean you train it one sample at a time?
    - How can it have any spatial awareness if this is the case.
    - It doesn't, the 256 in are real values and the 256 out is a one hot encoding of the middle sample prediction.
* How many layers should I be looking at?
    - 4-12 as a baseline.

# Next Steps

* Need to start looking at evaluation methods and collating data.
* Need to create a plan for the dissertation
* Work on implementation concurrently.
