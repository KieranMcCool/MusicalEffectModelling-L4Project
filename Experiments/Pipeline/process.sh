echo $(find dataset -iname \*.wav -exec echo "$(pwd)/{}\n"  \;) "<CONFIG
FXCHAIN \"$(pwd)/reverb.RfxChain\"
OUTPATH \"$(pwd)/dataset/out\"
>" > reaper && /Applications/REAPER64.app/Contents/MacOS/REAPER -batchconvert reaper
