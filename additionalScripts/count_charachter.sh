#!/bin/bash

CHAR=$1
FILE=$2

sed 's/[^'$CHAR']//g' $FILE | awk '{ print length }'
