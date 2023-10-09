#! /usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 22
fi

# if you're using a language other than Python 3, you will need to alter
# the lines below starting with `python 3`
if [ $1 == "tm_to_ptm" ]; then
    # Problem 4.1
    python3 problem_4_1.py
elif [ $1 == "ptm_to_tm" ]; then
    # Problem 4.2
    python3 problem_4_2.py
fi

# python, java, c, c++, haskell are supported
# for anything else, please ask staff
