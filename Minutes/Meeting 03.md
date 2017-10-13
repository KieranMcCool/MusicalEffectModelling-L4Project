% Minutes from Meeting 3
% Kieran McCool
% 28 September 2017

# Progress since last meeting

* Digitised meeting minutes and time log, both on Github repository
* Read the Unreasonable Effectiveness of Recurrent Neural Networks.
* Read Chris Olah's blog on LSTM
* Considered the effects I would like to model.
    - Thinking distortion would be a good starting point, TS808 VST Plugin since it's an effect pedal I'm familiar with.
    - Using success and experience gained with distortion, moving into some kind of time based effect like Chorus or Phaser would be appropriate.
    - Given the drastically different effects here, success with both would probably suggest that the method is suitable for a range of different effects.

# Questions

* Was having a hard time understanding what my inputs would be to the neural networks, would I use frequency and amplitude or would some kind of formula need to be applied to the data?
    - Initially amplitude over time would be a suitable format, however there are more advanced ways such as short time Fourier transform.
* Was wondering about training time, blogs mention leaving the network to train overnight on powerful GPUs, is this going to be true for my project?
    - Training times can be long and a GPU really helps.
    - Might be worth setting up SSH access on my gaming rig and do most of my work on there.
    - Will also have access to a GPU cluster at the university.
* Purely out of curiousity, was looking at the Kemper profiling amplifiers and wondering if they used machine learning as a basis for how they work.
    - Similar product to the Nebula VST plugin, probably uses the same method of Volterra Kernel Sampling to model some non-linear aspects of equipment.
    - Largely irrelevant but could be cool to draw a comparison in dissertation to show how my solution differs, and the weaknesses or strengths of it vs these solutions.

# For next week

* Work on getting a data pipeline for generating test data
    - Mrs Watson a command line utility for running VST plugin might be a good option here.
* Getting some practical experience with PyTorch using tutorials
    - http://pytorch.org/tutorials/
    - https://cs231n.github.io/
    - http://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
