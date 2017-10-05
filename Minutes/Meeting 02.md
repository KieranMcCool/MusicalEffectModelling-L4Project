% Minutes from Meeting 2
% Kieran McCool
% 28 September 2017

# Progress since last meeting

* Obtained a general understanding of neural networks
    - How they work, underlying principles
    - Obtained through reading literature and viewing lectures/screencasts on YouTube
* Prepared Geography presentation on project
    - Meant identifying aims/objectives/challenges/etc
* Setup PyTorch, had trouble installing Keras

# Questions

How involved should I get with the low level maths that drive machine learning?

* Operating at a high level so only basic understanding of what's going on required.
    - No need to learn proofs or have demonstrable knowledge of advanced concepts

Unsure about structure of neural networks, how are the layers generated, is this consciously created or automatic?

* You specify the structure, e.g. how many hidden layers etc and the rest is handled by the library.

# For next week

* Intending on completing PyTorch tutorial.
* Look into Recurrent Neural Networks
    - LSTM in particular
    - See 'The Unreasonable Effectiveness of Recurrent Neural Networks' for details
* Convolutional Neural Networks may also be used
    - 1 dimensional for sound wave rather than 2D which is case for image recognition.
* Generation of audio using Numpy and SciPy.
    - Outputting sin wave with increasing frequency as input data.
* Identifying problems
    - Which effects to model?
    - Where the effect will come from? VST Plugins? Hardware?
    - If VST, Renderman is a python library which can host VST plugins. Could automate the process using this.



