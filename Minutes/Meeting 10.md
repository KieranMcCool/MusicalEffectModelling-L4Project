% Minutes from Meeting 10
% Kieran McCool
% 30 November 2017

# Progress since last meeting

* Convolutional layers are now present
    - Weird errors with previous method of going 200x64x1, stated it expected a 3D Tensor, even though this is 3D.
    - Got around bug by wrapping all data in an additional dimension, reads as 4D but seems to work...
    - Loss is going lower than it has been previously and results are promising.
* New network 
    - Conv1D (64) -> ReLU ->Conv1D (32) -> ReLU ->  Conv1D(1)

# Next Steps

* Want to spawn new process for test output so it doesn't detract from training time.
* Experiment with parameters/network structure
    - Striding, etc
* Want to look at RNN/LSTM
* Starting to think about dissertation structure
* Some refactoring to save disk space and quality of life

# Notes

* Batch norm and dropout, strange behaviours could be result of overfitting
* Write loss out to file and plot to confirm overfitting
* More training data, real world music
* Predicting more outputs at a time is possible, could improve speed.
    - 64 inputs - 32 outputs
* For dissertation discussion, could pick 8 effects and ML viability
* Melspectogram (see librosa docs) for analysis
* Give data as large batches
    - Random sampling instead of sequential could improve results
