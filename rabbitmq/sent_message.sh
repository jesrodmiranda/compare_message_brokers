#!/bin/bash
for i in {1..500}
do
   echo "Welcome $i times"
   python new_message.py "A test message to MUY $i"
   sleep 0.05
done