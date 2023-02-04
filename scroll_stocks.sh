#!/bin/bash

zscroll -l 40 \
        --delay 0.1 \
        --match-command "`dirname $0`/get_stocks.sh" \
        --update-check true "`dirname $0`/get_stocks.sh" &
wait
