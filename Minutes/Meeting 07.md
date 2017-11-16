% Minutes from Meeting 5
% Kieran McCool
% 2 November 2017

# Progress since last meeting

* Changed pipeline to use Reaper batch converter instead of MrsWatson
    - Feature is poorly documented so some trial and error was required.
    - Difficulty with sample depth, scipy can't read 24 bit files which is the default for Reaper.
    - Overcome using render presets
* Reimplementation of the data generation script
    - Much more random/varied datasets in output.
    - Less repetitive
* First working model of a network running over the test data.
    - 2 Linear layers and 1 reLU layer
    - Loss does decrease but only a little bit. 
    - Want to encapsulate data in classes to monitor loss, let's us see which files it's good and bad at.

# Questions

* Fluctuations in loss across different files - does this indicate overfitting?
    - Probably due to network structure being over simplistic.
* Deciding on network structure
    - Smaller data slices, 64 input vector with 1 output, output being middle value of slice.
    - Allows for spatial awareness of what is happening around a given sample.
    - A different approach could be Conv1d (32 feat map) - Maybe 2 or three convs -> reLu (128) -> reLu (8)
    - Strided convolutions as a research avenue
        - Allows for gaps in data.

# For next week

* Work on getting the sliding window approach adapted for 64 into 1
* Get network ready for 64 to 1
* Get network outputting data
