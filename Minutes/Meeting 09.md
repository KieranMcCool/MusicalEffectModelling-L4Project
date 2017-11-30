% Minutes from Meeting 09
% Kieran McCool
% 23 Nov 2017

# Progress since last meeting

* Slow week, assessments etc.
* Model checkpoints at configurable intervals
    - No way to load from checkpoint yet unless you hard code it in net.py
* Ran network a few times with cleaner test data and simpler effect.
    - Reaper Linear distortion unit
    - Clean guitar, previous sample was on the edge of clipping/distorting at points, made it difficult to tell if network was getting better or not.
* Verified model is working by training to reproduce input.
    - This was verified as loss dropped to 0 very quickly and stayed there.
* Tried to introduce more sophisticated model through convolutional layers
    - Conv1D layer takes multiple input planes, my sound data is just 1. 
    - Not sure how to get around this? Where do they additional input planes come from?

# Clarification of Conv1d Layer

* C = channels = 1
* N = Batch Size = 32
* L = No. Inputs = 64
* Need a 300x64x1 tensor
* 64 input size to 32
* Kernel size = 3

# Wavenet Paper

* Useful to read this
* Deals with audio data as a classification problem rather than a prediction one.
    - Instead of getting one output, we get a tensor of size representing the bit-depth then select the bit with the highest probability as our output.
