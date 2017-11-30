% Minutes from Meeting 6
% Kieran McCool
% 2 November 2017

# Progress since last meeting

* Adapting network for audio data.
    - Slicing wav files into segments of equal size, padding if necessary
    - Basic functionality of iterating over the data is mostly in tact, I just need data to test with...
* Hit a bit of a snag in that MrsWatson is not working as it should.
    - Processing with MrsWatson adds significant hiss and decreases overall recording quality greatly.
    - Originally thought this was an issue of default effect parameters, it's not. Using FXP file from Reaper yields same result.
    - Tried various workarounds, nothing made it better. Different effects, using actual music, etc.
    - Tried installing RenderMan as an alternative, with no avail, wasted a lot of time trying to compile it.
    - Thought about trying data of YouTube as it's plentiful and if worst case scenario, I wouldn't mind running manually on it as long as the files were big and few.

# Questions

* How to progress with test data
    - Probably for now, best to work from manually created data while we explore options.
    - Reaper has a scripting language, could be useful
    - Have another go with RenderMan?
* Data from YouTube sufficient?
    - Probably not, might be repetitive etc.

# For next week

* Attempt to work through data problems
* Apply neural network to training data.
