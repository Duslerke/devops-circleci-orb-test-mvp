#!/bin/bash

#>>Script1<<#
function spamTheScreen() {
    for i in $(seq $1 $2); do
        a[i]=$i
    done
}

spamTheScreen 0 100

#>>Script1<<#
