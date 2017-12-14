rm -rf dataset
rm -rf model_outputs

mkdir dataset
mkdir model_outputs

./main.py -n $1 -s $2

echo $(find dataset -iname \*.wav -exec echo "$(pwd)/{}\n"  \;) \
    "<CONFIG
    FXCHAIN \"$(pwd)/$3\"
    OUTPATH \"$(pwd)/dataset/processed\"
    <RENDERPRESET render 0 0 0 0 3 0>
    >" > reaper \
&& /Applications/REAPER64.app/Contents/MacOS/REAPER -newinst -batchconvert reaper

find ./dataset/processed/ -name '*.wav' |  while read line ; do
mv "$line" "$(echo $line | sed 's|/- ||g')";
done;

cp ./testfiles/* ./model_outputs/

echo $(find model_outputs -iname \*.wav -exec echo "$(pwd)/{}\n"  \;) \
    "<CONFIG
    FXCHAIN \"$(pwd)/$3\"
    OUTPATH \"$(pwd)/model_outputs/processed\"
    <RENDERPRESET render 0 0 0 0 3 0>
    >" > reaper \
&& /Applications/REAPER64.app/Contents/MacOS/REAPER -newinst -batchconvert reaper

find ./model_outputs/processed/ -name '*.wav' |  while read line ; do
mv "$line" "$(echo $line | sed 's|/- ||g')";
done;

rm reaper
rm reaper.log
