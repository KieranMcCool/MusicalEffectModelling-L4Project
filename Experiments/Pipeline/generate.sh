rm -rf dataset

mkdir dataset

./main.py -n $1 -s $2

echo $(find dataset -iname \*.wav -exec echo "$(pwd)/{}\n"  \;) "<CONFIG
FXCHAIN \"$(pwd)/$3\"
OUTPATH \"$(pwd)/dataset/processed\"
<RENDERPRESET render 0 0 0 0 3 0>
>" > reaper && /Applications/REAPER64.app/Contents/MacOS/REAPER -newinst -batchconvert reaper

find ./dataset/processed/ -name '*.wav' |  while read line ; do
mv "$line" "$(echo $line | sed 's|/- ||g')";
done;

echo $(find model_outputs -iname \*.wav -exec echo "$(pwd)/{}\n"  \;) "<CONFIG
FXCHAIN \"$(pwd)/$3\"
OUTPATH \"$(pwd)/model_outputs/processed\"
<RENDERPRESET render 0 0 0 0 3 0>
>" > reaper && /Applications/REAPER64.app/Contents/MacOS/REAPER -newinst -batchconvert reaper

find ./model_outputs/processed/ -name '*.wav' |  while read line ; do
mv "$line" "$(echo $line | sed 's|/- ||g')";
done;
