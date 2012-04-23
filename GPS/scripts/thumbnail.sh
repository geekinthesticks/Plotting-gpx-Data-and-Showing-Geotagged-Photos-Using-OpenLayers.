#!/bin/sh

FILES="$@"
for i in $FILES
do
echo "Prcoessing image $i ..."
/usr/bin/convert -thumbnail 75 $i thumb.$i
done
