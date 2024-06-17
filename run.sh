#!/bin/bash

# Initialize an empty array to store commands
commands=()

# Read the file line by line and store each line in the array
while IFS= read -r line; do
    commands+=("$line")
done < command.txt

# Delete any file ending with "oauth2.json" first
find . -type f -name '*oauth2.json' -exec rm -f {} \;

# Iterate over each command and execute it
for ((j=0; j<${#commands[@]}; j++))
do
    command="${commands[j]}"
    
    echo "Executing: $command"
    eval $command
    if [ $? -eq 0 ]; then
        echo "Successfully executed: $command"
    else
        echo "Failed to execute: $command"
    fi
    
    # Delete any file ending with "oauth2.json" every 5 commands
    if (( (j + 1) % 5 == 0 )); then
        find . -type f -name '*oauth2.json' -exec rm -f {} \;
    fi
done
