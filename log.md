## 29/09/2017 - 3 Hours

* Began reading the first chapter of colah.github.io
* Watched YouTube Lectures on machine learning and neural networks

## 03/10/2017 - 2 Hours

* Read some of Section 1 of Nielson's book on machine learning

## 04/10/2017 - 2 Hours

* Prepared presentation on project for Advanced Geographies Presentation
* Installed PyTorch successfully
* Had trouble with Keras installation.

## 05/10/2017 - 2 Hours 

* Second project meeting
* Began reading "The Unreasonable Effectiveness of Recurrent Neural Networks."
* Spent time looking for tutorials on using PyTorch.

## 11/10/2017 - 2 Hours

* Moved Keras and PyTorch installations from using system Python and Pip to Anaconda virtual environment.
* Reread "The Unreasonable Effectiveness of Recurrent Neural Networks"
* Read Chris Olah's blog post on LSTM Netorks

## 12/10/2017 - 1 Hour

* Third project meeting
* Digitised minutes from today's meeting.

## 13/10/2017 - 2 Hours

* Started working on pipeline for generating test data
    - SciPy for generating wav files, Mrs Watson for processing them through the VST plugin.
    - Having trouble getting Mrs Watson to read the wav files generated.

## 17/10/2017 - 3 Hours

* Test data pipeline is mostly in place, just working out some bugs with MrsWatson.
	- MrsWatson processes the files and data looks to be there but no software can seem to read the resulting files...
	- Might try with MacOS/Windows instead of Linux as these appear to be better supported.
	- Choice of plugins also limited by poor support on Linux from VST developers.
    - Frustratingly, everything worked with only minor changes on Windows.
* Upon hearing the output from the VST plugins, I decided to move away from random frequency sweeps to those found within a guitars frequency range.
    - Researched what this range was and wrote code to replicate it.
* Looking at setting variables on effect with MrsWatson.

## 18/10/2017 - 1 Hour

* Worked through introduction PyTorch tutorials on their website.

## 19/10/2017 - 1 Hour

* Wrote up minutes from Meeting 4
    - Also fixed dates of meeting minutes, I had been forgetting to change them.

## 23/10/2017 - 1 Hours

* Cleaned up code for test data pipeline, almost ready to be finalised into a python CLI program.
* Read additional documentation for PyTorch

## 24/10/2017 - 2 Hours

* Followed PyTorch examples until intermediate
* Read some blogs about PyTorch
    - [](https://www.oreilly.com/ideas/why-ai-and-machine-learning-researchers-are-beginning-to-embrace-pytorch)

## 25/10/2017 - 2 Hours

* Adapting basic neural network from tutorials into something which can accept the wav data as read by SciPy
    - Reading in wav files with SciPy as Numpy arrays, converting to PyTorch tensors.
