#!/bin/bash

USAGE="
    USAGE:
      - Options
        -> ./unzip.sh -h, --help
        -> ./unzip.sh -y, --year <year> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
        -> ./unzip.sh -ym, --year-month <year>-<month> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
"
HELP="
    unzip.sh

    DESCRIPTION
      - This script unzips log files based on specified criteria.

      - The script will scan over INPUT_PATH directory:
        - The log file names MUST follow this format: *yyyy-mm-dd*

      - The script will unzip on OUTPUT_PATH directory:
        - OUTPUT_PATH/yyyy/mm/yyyy-mm-dd.log

    USAGE
      - Options
          -> ./unzip.sh -h, --help
              Show this help message

          -> ./unzip.sh -y, --year <year> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
              Unzip files for a specific year

          -> ./unzip.sh -y, --year-month <year>-<month> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
              Unzip files for a specific year

    DEPENDENCIES
      - No external dependencies are needed
"

echo "$HELP"

exit 0

INPUT_PATH=/mnt/working/logsanon
OUTPUT_PATH=/mnt/working/github/OSTIA/res

mode=$1
date=$2



elif [[ $mode != "year-month" && $mode != "year" ]]; then
    echo "Invalid mode. Please choose either 'year-month' or 'year'."
    exit 1
fi

exit 0

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
