template="% Minutes from Meeting {NUMBER}
% Kieran McCool
% {DATE}

# Progress since last meeting

# Next Steps

# Notes
"
n=`let "x=$(ls -1 | grep Meeting | sed "s|Meeting ||g" | sed "s|.md||g" | tail -n 1 | sed "s/^0*//") + 1" && printf "%02d" "$x"`

d=$(date | python -c "from sys import stdin; print(' '.join(stdin.read().split(' ')[1:4]));") 

echo "$template"| sed "s|{DATE}|$d|g" | sed "s|{NUMBER}|$n|g" > "Meeting $n.md"
