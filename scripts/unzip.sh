#!/bin/bash

INPUT_PATH=/mnt/working/logsanon
OUTPUT_PATH=/mnt/working/github/OSTIA/res

mode=$1

if [[ $mode == "year-month" ]]; then
    read -p "Enter the date in the format yyyy-mm: " input_date
elif [[ $mode == "year" ]]; then
    read -p "Enter the year in the format yyyy: " year
else
    echo "Invalid mode. Please choose either 'year-month' or 'year'." && exit 1
fi

# -----------------------------------------------------------------------------

if [[ $mode == "year-month" ]]; then
    logs=$(ls $INPUT_PATH | grep $input_date)
    year=$(echo $input_date | cut -d'-' -f1)
    month=$(echo $input_date | cut -d'-' -f2)
    mkdir -p $OUTPUT_PATH/$year/$month

elif [[ $mode == "year" ]]; then
    logs=$(ls $INPUT_PATH | grep "^$year-")
    for month in {01..12}; do
        mkdir -p $OUTPUT_PATH/$year/$month
    done

fi

# -----------------------------------------------------------------------------

process_logs() {
    local logs="$1"
    local output_dir="$2"

    while IFS= read -r line; do
        date=$(echo $line | cut -d. -f2)
        echo "unzip $line ..."
        gunzip -c $INPUT_PATH/$line > $output_dir/$date.log
    done <<< "$logs"
}

# -----------------------------------------------------------------------------

if [[ $mode == "year-month" ]]; then
    process_logs "$logs" "$OUTPUT_PATH/$year/$month"

elif [[ $mode == "year" ]]; then
    for month in {01..12}; do
        logs=$(ls $INPUT_PATH | grep "$year-$month")
        process_logs "$logs" "$OUTPUT_PATH/$year/$month"
    done
fi

#TODO: check if folder / logs already exists
