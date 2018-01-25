% Minutes from Meeting 12
% Kieran McCool
18 Jan 2018

# Progress since last meeting

* DataLoader used instead of my own method
    - Wrote a class which handles my dataset and extends the PyTorch DataLoader class
    - Benefit of being automatically parallelised by PyTorch
    - Different samplers can be used easily
    - I wrote my implementation to be specifically lazy, which saves a lot of memory vs what I had.
* Experimented with larger input vectors into convolutional layer in hopes that it would allow it to learn time based effects.
    - 1500 samples, 100 batches. This is the hardware limit which my computer can handle.
    - Network does start to learn some characteristics of the effects. However, it distorts and there are clear artifacts.
    - Not sure why this happens...
* Experimenting with LSTMs
    - Don't show signs of progress compared to convolutional network.
    - Figured I'd need to use sequential sampling instead of random so it could learn the time element to the data.
    - Sequential Sampling seems to overfit as network shows miniscule loss on test data but produces lots of noisy data. Clicks/Pops/Static sounding noises.
    - Think I need to write a sequential sampler that gives n sequential elements then changes it's position in the dataset randomly.
    - Messed with LSTM -> Linear, Linear -> LSTM etc. Didn't help

# Next Steps

* Back to basics with LSTM
    - 1 sample input -> 1 sample output
    - Back to just a single LSTM layer.
* For Convolutional network, could have a sliding window output too. Average in between values over windows.
    - Could help with the gain we seem to end up with on these networks.
