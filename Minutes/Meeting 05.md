% Minutes from Meeting 5
% Kieran McCool
26 October 2017

# Progress since last meeting

* Not a particularly productive week being honest.
* Worked through some more PyTorch Tutorials
* Have a template of a simple network that I can see how to apply to sound data.
    - Problems with duration variation, seems to be a problem for some other similar projects
* Found a GitHub repo 'Awesome PyTorch List' with lots of blogs/tutorials/libraries/projects that could be good for code examples or inspiration.
    - Of particular interest is DeepSound, a similar project to this one only it is designed to replicate music in general rather than effects.
    - Also some libraries which could be helpful, including one which can read a host of sound formats and convert them straight into PyTorch tensors.
* Also spend a little time playing with PyTorch in an iPython console, tabbing through and googling functions, classes that looked interesting/useful.

# Questions
 
* How to handle variable duration of audio samples
    - Dividing file up into blocks, sliding window approach.
    - Might be good to use DeepSound as a template here as they overcame the issue.
* Some of the tutorials on PyTorch stated that they were overly simple and were guilty of overfitting. How do I avoid this with my project?
    - The key is to have a large and varied set of training data.

# For next week

* Aim to have an implementation of the sliding window approach
* Would be good to have some kind of network up and running and processing sound data.
* Think about additional test data, randomisation etc.
* Again, automate as much as possible.
