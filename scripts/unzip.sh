#!/bin/bash

VERSION=1.2.0
LAST_DATE=2024-05-10

USAGE="
    USAGE:
      - Options
        -> ./unzip.sh -h, --help
        -> ./unzip.sh -y, --year <year> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
            -> year: yyyy
        -> ./unzip.sh -ym, --year-month <year>-<month> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
            -> year-month: yyyy-mm
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

          -> ./unzip.sh -ym, --year-month <year>-<month> -i, --input-path <INPUT_PATH> -o, --output-path <OUTPUT_PATH>
              Unzip files for a specific year

    DEPENDENCIES
      - No external dependencies are needed
"

# ----------------------------------------------------------------------------- #

MODE=""
YEAR=""
MONTH=""
INPUT_PATH=""
OUTPUT_PATH=""

if [[ $# -eq 1 ]]; then
    if [[ $1 == "-h" || $1 == "--help" ]]; then
        echo "$HELP"
    else
        echo "$USAGE"
    fi
    exit 0
fi

if [[ $# -ne 6 ]]; then
    echo "$USAGE"
    exit 1
else
    if [[ $1 == "-y" || $1 == "--year" ]]; then
        YEAR="$2"
        MODE="year"
    elif [[ $1 == "-ym" || $1 == "--year-month" ]]; then
        YEAR=$(echo "$2" | cut -d'-' -f1)
        MONTH=$(echo "$2" | cut -d'-' -f2)
        MODE="year-month"
    else
        echo "$USAGE"
        exit 1
    fi

    if [[ $3 == "-i" || $3 == "--input-path" ]]; then
        INPUT_PATH="$4"
    else
        echo "$USAGE"
        exit 1
    fi

    if [[ $5 == "-o" || $5 == "--output-path" ]]; then
        OUTPUT_PATH="$6"
    else
        echo "$USAGE"
        exit 1
    fi
fi

# ----------------------------------------------------------------------------- #

process_logs() {
    local logs="$1"
    local output_dir="$2"

    while IFS= read -r line; do
        date=$(echo "$line" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
        echo "unzip "$line" ..."
        gunzip -c $INPUT_PATH/$line > $output_dir/$date.log
    done <<< "$logs"
}

create_directory() {
    local year="$1"
    local month="$2"

    if [[ ! -d "$OUTPUT_PATH/$year/$month" ]]; then
        mkdir -p $OUTPUT_PATH/$year/$month
    else
        echo "ERROR | "$OUTPUT_PATH/$year/$month" already exists"
        exit 1
    fi
}

# ----------------------------------------------------------------------------- #

if [[ $MODE == "year-month" ]]; then
    logs=$(ls "$INPUT_PATH" | grep "$YEAR-$MONTH")
    if [[ -n "$logs" ]]; then
        create_directory "$YEAR" "$month"
        process_logs "$logs" "$OUTPUT_PATH/$YEAR/$month"
    fi

elif [[ $MODE == "year" ]]; then
    for month in {01..12}; do
        logs=$(ls $INPUT_PATH | grep "$YEAR-$month")
        if [[ -n "$logs" ]]; then
            create_directory "$YEAR" "$month"
            process_logs "$logs" "$OUTPUT_PATH/$YEAR/$month"
        fi
    done
fi
