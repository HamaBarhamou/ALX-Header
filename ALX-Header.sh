#!/bin/bash

if [ -e $1 ]
then
    python3 main.py $1
else
    echo "The file does not exist "
fi

