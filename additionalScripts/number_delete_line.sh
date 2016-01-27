#!/bin/bash

FILE=$1
LINE=$2
LINE_DELETE="${LINE}d"
sed -i.bak $LINE_DELETE $FILE
