% Minutes from Meeting 1
% Kieran McCool
% 28 September 2017

# Introduced concepts

- Looking at Deep Learning
- Mapping transformations from clean input (No effect) to modelled effect.
* Types of effects
    - Distortion, chorus, tape decks, reverb, etc.
    - How far do we want to go? Do we look into modelling the parameters (dials/buttons/etc) on the effects units?
* Software/Technology
    - Python good option: Libraries like Keras and PyTorch.
* Project N-Synth on GitHub, similar application of machine learning, might have some good literature.
* Bibliography management tools for managing literature read.
    - Zotero recommended

# Potential Capturing Methods

* Sofware effects will be easier
    - Easy to generate output
    - No need to worry about sample time
* Modelling of analogue/hardware effects possible by outputting a sin wave from sound card, running into effect unit then sampling the output back into the line in.
    - Potential trouble with sample time.
* Dataset is going to be the key to the success of this project so it's important to get this right.

# Evaluating Success

* How do we evaluate whether or not we're modelling the effect accurately?
    - Feedback from knowledgeable listeners?
    - Signal analysis?
