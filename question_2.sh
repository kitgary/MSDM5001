#!/bin/bash

for i in {1..100}
do
	folder="DDM$i"
	mkdir $folder
	date=$(date "+%s%N")
	echo -e "nanoseconds since 1970-01-01 00:00:00 UTC:\n$date" > $folder/time_till_now.txt
done

