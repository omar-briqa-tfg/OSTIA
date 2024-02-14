#!/bin/bash

INPUT_FILE=../res/input.log

while IFS= read -r line
do
    echo $line
done < "$INPUT_FILE"