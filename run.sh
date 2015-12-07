#!/bin/bash

for i in `seq 0 9`;
do
	python index.py "$1/subset$i.txt"
done