#!/bin/bash
source ./init.sh

list=$(pgrep -f logstash)

echo $list

if [ -n "$list" ]
then
    echo "Running logstash"
    exit 0
fi
exit 1

