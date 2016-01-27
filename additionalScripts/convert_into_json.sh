#!/bin/bash

sed -i.bak 's/$/,/' $1
rm -f "$1.bak"

NAME=`echo $1 | cut -d'.' -f1`
LAST="${NAME}_real.json"

echo [ >> $LAST
sed '$ s/.$//' $1 >> $LAST
echo ] >> $LAST

rm -f $1
mv $LAST $1

echo "Your file" $1 "now is a JSON file"
