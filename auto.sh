#!/bin/bash

# tests

RED='\033[1;31m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SAMPLE_DATA="sample-data"

FAILED=0
PASSED=0

rm -f compressed.out1
rm -f decompressed.out
rm -f diff.out

for entry in `find "${SAMPLE_DATA}" -name '*.txt'`
do
    echo -e "${BLUE}$entry${NC}"
    
    echo -e "${YELLOW}compressing${NC}"

    time python3 main.py -c "$entry" compressed.out

    echo -e "${YELLOW}decompressing${NC}"

    time python3 main.py -d compressed.out decompressed.out

    echo -e "${YELLOW}diffing${NC}"
    
    echo "orignal file:"
    ls -lh "$entry" | cut -d" " -f9
    ls -l "$entry" | cut -d" " -f8
    echo "compressed version:"
    ls -lh compressed.out | cut -d" " -f9
    ls -l compressed.out | cut -d" " -f8
    echo "decompressed version:"
    ls -lh decompressed.out | cut -d" " -f9
    ls -l decompressed.out | cut -d" " -f8

    diff -Bb decompressed.out "$entry" &> diff.out

    ret=$?
    if [ $ret -ne 0 ]; then
        echo -e "${RED}FAIL!${NC}"

        echo
        echo -e "${BLUE}DIFF${NC}"
        echo
        cat diff.out

        (( FAILED++ ))
    else
        echo -e "${GREEN}PASS!${NC}"

        (( PASSED++ ))
    fi

    echo
    echo "-----------------------------------------------------------------------------------------------"
    echo

    rm -f compressed.out
    rm -f decompressed.out
    rm -f diff.out
done

rm -f compressed.out
rm -f decompressed.out
rm -f diff.out

echo -e "${RED}FAILED${NC}: ${FAILED} tests"
echo -e "${GREEN}PASSED${NC}: ${PASSED} tests"
