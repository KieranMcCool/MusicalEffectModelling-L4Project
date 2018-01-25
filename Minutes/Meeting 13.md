% Minutes from Meeting 13
% Kieran McCool
% 25 Jan 2018

# Progress since last meeting

* Wrote random sequential sampler
    - Configurable sequence lenght (currently 5 seconds as I feel this is enough time for the time-dependent effects to express themselves.)
    - Uses list generators so it's fast and memory efficient!
    - Also doesn't sample the same sequence more than once, so we shouldn't have issues with overfitting.
* Hoped that RS Sampler would make LSTM learn better but it's still suffering the same problems
* Convolutional Network still working reliable :)
    - Collected some sample sounds for ABX testing at a later date.
    - Light and heavy distortion
* Generated some signal chains for use in training different effects.
* Touched up the generate script as it has been untouched since I wrote it and I'm now a lot better at bash scripting than I was...
    - It has functions and code reuse now!! :)

# Next Steps

* For LSTMs
    - Much larger hidden size, maybe 200-2000
    - Number of layers should be 2 - 6 as a baseline
    - Output will be a (BatchSize x 200) tensor, which I should feed to a fully connected layer.
* Report loss relative to expected output to make it a more useful measure?
* Spend next few days with LSTM but time is marching on so it might be a good idea to have a fallback
* Nebula plugin as a case study?
    - Find out what it claims to do well and evaluate if my network is comparable.
* There is probably parts of the dissertation which I should be able to write just now, might want to start looking at that.
