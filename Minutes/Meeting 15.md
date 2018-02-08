% Minutes from Meeting 15
% Kieran McCool
% 8 Feb 2018

# Progress since last meeting

LSTM Status

* Found a few examples using the LSTMCell instance instead of LSTM.
    - Difference being LSTM allows multiple layers, wherease with LSTMCell you have to stack them yourself.
    - LSTMCell has no GPU acceleration support.
    - Generally not advised to use...
    - I haven't got it working yet either... Can train but it wont output the file properly.

Nebula Case Study

* Version 2 using Voltera kernels to capture non-linear behaviours with a memory-like property.
    - Makes it a step above traditional VSTs for things like tape delay with subtle time dependent effects.
    - Also captures non-linearity of distortions and amp sims quite well.
* A lot of criticism for being unstable and difficult to use.
    - Lots of people claiming that it doesn't work / is unreliable and lots of other people telling those people that they just don't know how to use it properly.
* CPU intensive, a lot of criticism for this.
* Downloaded the trial version, going to have a play with it.
* Version 3 getting really good reviews using 'dynamic convolutions', however this technique is patent protected and I can't find any specific information on it.

Impulse Response Monitoring

* Played with Reaper's Impulse monitoring VST.
    - Can combine model output to left channel and vst output to right channel and view both curves.
    - I've only tried this on some distortion outputs but they look really close, model output might tend to peak a little higher but generally a good match.
    Really want a way of automating this

# Final Effects

Splitting into categories:

Filters:

* Low pass filter
* High pass filter
* Realistically, I can't replicate a use case for those.
* Noise gate - That one's easy, just add use some heavy gain on a single-coil pickup and I'll have loads of hiss to remove.

Distortion/Boost

* TS808 - Several different settings I want to try and replicate. 
    - Classic TS808 sound: mid-boosted and medium gain (clean if you pick softly). 
    - The VST I'm using gets pretty crazy with the gain up all the way, might be cool to try that. 
    - Also can be used a lot more subtly as a mid-boost with low gain.
* Fuzz - Probably some kind of fuzz face clone. 
    - Could be interesting to see how the network learns how sensitive fuzzes are to input volume, lots of dynamic range.
* Compressor - I actually think this might be difficult for the network to learn since it's not just a case of boosting the amplitude or filtering out certain frequencies. 
    - Some things will need boosted and others will need softened.

Time-Based Effects

* Reverb : A few different reverbs that I'm looking at, was hoping for a nice spring reverb VST but I can't find one I like... Think I'm going to stick with algorithmic reverbs for this as a result - of which there are many that sound decent.
* Chorus - I have a chorus VST I've been using that I quite like so far. 
    - Might try 6 different presets for chorus, shallow fast modulation, deep slow modulation, deep fast etc
    - Doubtful of success at this point with LSTM failure...
* Delay: No shortage of plugins here...
    - Similar setup to chorus with 6 combinations of short time short low number of repeats etc.

Time permitting, it might also be cool to see if we can train models separately and create a workable signal chain.
    - Would also demonstrate how effective the models actually are by testing them in a way that they could not train for.

# Next Steps

* Create the models for the effects and gather test data.
* Look into automating impulse response analysis.
* Choose ABX testing software
    - Ideally something web-based as this would allow much more data to be gathered via forums/facebook group etc
    - I do also have some people that I want to get to do the test in person, so if I can't get a web-based solution then I'll at least have some results.
    - Need to create maybe 5 to 10 second samples of input, vst output and model output on the same track for evaluation.

# Notes

* Filters - Carefuly with choices, hard to model filters.
    - Impulse response, modelling non-linearity.
* Voxengo Fuzz, Guitar amp simulator, boogex.
* Regular and multiband compressor.
    - 3 Band compressor.
* Delay less interesting.
    - Could do dub delay, saturation and frequency distortion.
* Train signal chain end-to-end.
* Lacinato cloud based ABX testing
* Dilated convolutions.
* Wavenet, classifications as 8 bit.
    - Have a careful read of it.

