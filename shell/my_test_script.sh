#!/bin/bash

#>>Script1<<#

function spamTheScreen() {
    for i in $(seq "$1" "$2"); do
        # shellcheck disable=SC2034
        a[i]=$i #if you think that it's false positive
        echo "current number is: $i"
    done
}

echo "{a[*]}"

#Oh btw, this code contains this operator << omg, circle ci will break now
#Unless I escape << it with \<<, this requires automation, however.
#And escaping it in code, will prob just make the shell crash, when you test it anyway!!!
#Let's <<  <<  <<  <<  <<  <<  << see it break, if it doesn't I'll add an actual operator

spamTheScreen 0 100

#>>Script1<<#
