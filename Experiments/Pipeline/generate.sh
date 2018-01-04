rm -rf dataset
rm -rf model_outputs

mkdir dataset
mkdir model_outputs

cp training_music/*.wav dataset

# Generate Dataset
./main.py -n $1 -s $2

# Set up reaper batch file
find dataset -iname \*.wav -exec printf "%q\n" `winepath -w {}` \; | tr -d "'" > reaper
echo "<CONFIG
    FXCHAIN \"$(winepath -w $(pwd)/$3)\"
    OUTPATH \"$(winepath -w $(pwd)/dataset/processed)\"
    <RENDERPRESET render 0 0 0 0 3 0>
>" >> reaper

# run reaper
wine ~/.reaper_install/reaper.exe newinst -batchconvert $(winepath -w reaper)

# rename output files
for f in ./dataset/processed/*.wav; do
    mv "$f" "$(echo $f | sed 's|- ||g')"
done;

# Populate test files
cp ./test_files/* ./model_outputs/

# Set up reaper batch file
find model_outputs -iname \*.wav -exec printf "%q\n" `winepath -w {}` \; | tr -d "'" > reaper
echo "<CONFIG
    FXCHAIN \"$(winepath -w $(pwd)/$3)\"
    OUTPATH \"$(winepath -w $(pwd)/model_outputs/processed)\"
    <RENDERPRESET render 0 0 0 0 3 0>
>" >> reaper

# run reaper
wine ~/.reaper_install/reaper.exe newinst -batchconvert $(winepath -w reaper)

# rename output files
for f in ./model_outputs/processed/*.wav; do
    mv "$f" "$(echo $f | sed 's|- ||g')"
done;

