#!/usr/bin/env bash

function setup {
    # Delete old directories if they exist (discard output)
    rm -rf dataset
    rm -rf model_outputs

    # Make necessary directories
    mkdir dataset
    mkdir model_outputs 
    mkdir training_music
    mkdir dataset/processed
    mkdir model_outputs/processed
    mkdir model_checkpoints

    # Populate pre-prepared data
    cp training_music/*.wav dataset
    cp ./test_files/* ./model_outputs/
}

function reaper {
    # $1 = Directory to search, #2 = signal chain
    # Set up reaper batch file
    find $1 -iname \*.wav -exec echo $(pwd)/{} \; | tr -d "'" > reaper
    echo "<CONFIG
        FXCHAIN \"$(pwd)/$2\"
        OUTPATH \"$(pwd)/$1/processed\"
        <RENDERPRESET render 0 0 0 0 3 0>
    >" >> reaper
    # run reaper
    /Applications/REAPER64.app/Contents/MacOS/REAPER -newinst -batchconvert reaper
    # rename output files
    for f in $1/processed/*.wav; do
        mv "$f" "$(echo $f | sed 's|- ||g')"
    done;
}

function reaperWine {
    # $1 = Directory to search, #2 = signal chain
    # Set up reaper batch file
    find $1 -iname \*.wav -exec printf "%q\n" `winepath -w {}` \; | tr -d "'" > reaper
    echo "<CONFIG
        FXCHAIN \"$(winepath -w $2)\"
        OUTPATH \"$(winepath -w $1/processed)\"
        <RENDERPRESET render 0 0 0 0 3 0>
    >" >> reaper
    # run reaper
    wine ~/reaper/reaper.exe newinst -batchconvert $(winepath -w reaper)
    # rename output files
    for f in $1/processed/*.wav; do
        mv "$f" "$(echo $f | sed 's|- ||g')"
    done;
}

function cleanup {
    rm reaper.log
    rm reaper
}

setup 2> /dev/null
# Generate Dataset
./genrate.py -n $1 -s $2
reaperWine dataset $3
reaperWine model_outputs $3
cleanup
