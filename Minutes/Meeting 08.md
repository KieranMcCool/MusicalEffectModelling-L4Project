% Minutes from Meeting 8
% Kieran McCool
% 16 November 2017

# Progress since last meeting

* Network now properly uses sliding window approach
    - 64 magnitude vector as input with target being the 32nd element
* A lot of code refactoring
    - Was difficult to reason about sliding window approach with previous method
    - Old code was memory inefficient
    - Now object based - data collection and analytics is much easier to implement
    - Globals file for common parameters - SampleRate etc
* Network can output it's prediction for a given wav file on request.
* Ran network on reverb a couple of times
    - First time was pretty unsuccessful due to lack of 'spatial awareness'
    - Tried again with a much larger time slice (44100 from 64) and had better results but still not great.
    - Linear network not great for reverb it seems
* Ran on TS808
    - More successful than reverb but definitely not perfect
    - Doesn't seem to get how it should vary the volume

# Next Steps

* More sophisticated network 
    - Convolutional layers and normalisation
* Save state : This is a priority
* More training time

# Questions

* Loss - Already really low but results aren't great
    - Suggests over-fitting is occurring.
    - Supplement training data with real world data perhaps?
    - Need to find a way to have training data have varied volume
* Time - Network is really slow to train
    - Will be better once we have convolutions etc


# Notes

* Try with simpler effects
* Dilation spaces out results could combat overfitting/lack of data
* Start with basic convolutional layers (Conv1D) 
* Check how loss is computed
    - Potentially incorrectly calculating loss on test set
    - Maybe overfitting
    - Regularisation - Dropout after every layer except last, batchnorm at start
* Think about results analysis
    - LibRosa for fourier transformations etc
    - Could graph over time with MatPlotLib
    - Comparisons?
    - Listening? 
