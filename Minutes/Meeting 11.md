% Minutes from Meeting 11
% Kieran McCool
% 7 December 2017

# Progress since last meeting

* Batches and random sampling implemented
    - Batch size of 100, 200 got poor performance and loss was not coming down as much as I'd like.
    - Batches really speed up the process of running sequentially over unseen data to produce model outputs. (To be expected since we're doing 100 samples at a time instead of just 1.)
    - Loss doesn't come down as much as it did before random sampling was implemented, this is also probably to be expected and the results are much better regardless of what the loss would imply
* Mel Spectogram visualisation for analysing outputs
    - Now got a quantitative measure of network progress.
* Started refactoring code to pave way for quality of life improvements.
    - Moving all non-ML code to main.py instead of net.py to prevent excessively long files
    - main.py will use argparse for arguments for ease of extensibility.
    - Cleaned up some hacky code.
* Explored network architecture
    - Tried to recreate wavenet network to an extent, 4 conv layers with dilation value doubling each layer, then into linear layers. Didn't see any noticeably improvement and performance suffered
    - Settled on current architecture Conv1D (64) -> ReLU -> Conv1D (32) -> ReLU -> Linear (32) -> ReLU -> Linear (16) -> ReLU -> Linear (1) -> Output
    - Seems to produce good results for TS808. 

# Next Steps

* Script for MP3 archival.
    - Wont use MP3s for ABY testing as compression could hinder the accuracy
    - LibRosa can read MP3s but can't write them so I'll need to use a bash script through ffmpeg or similar
* Play some more with network architecture
    - Input vector size, 64 was decided arbitrarily so there could be a better value.
* LSTM/Recurrent Networks
    - PyTorch seems to have these implemented as layers so hopefully shouldn't be too difficult to experiment with these.
* Feeling good about progress, confident trying with some additional effects
* Status report

# Notes

* DocOpt - Could be an alternative to ArgParse, generates a parser based on help file as txt.
* ABX Tester for Mac - Useful tool for evaluating success?
    - Lets me do ABX tests on files

## Dissertation Structure

* Introduction
* Background
    - Project Magenta
    - WaveNet
    - Nebula/Kemper
* Aims
    - What are we trying to achieve?
    - How will we know what success looks like?
* Methods
    - Network Architecture
    - Evaluating outputs, Mel Spectogram etc
* Implementation
    - PyTorch
    - SciPy.signal
    * LibRosa
    * Reaper and the VSTs used
    * How the pieces fit together
* Evaluation
    - Split into quantitative and qualitative   
    - Signal Analysis (Quantitative)
    - Spectogram GIFs (Quantitative)
    - Loss over time / Standard Deviation of loss ( ??? - Loss hasn't really proven to be particularly meaningful)
    - ABX tests with classmates/friends (Qualitative) 
* Conclusion

