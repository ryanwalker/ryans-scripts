#!/bin/bash

# Loop through all branches
for branch in $(git branch --format='%(refname:short)'); do
	echo "git branch -D ${branch}" >>  del
done
