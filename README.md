# 7BitEncoder
## What is this prodject

This prodject is based set up for basic SMS text message encoding and decoding.

## Current State

This project is currently under devolpment however it will be able to encode and decode simple messages

## Changelog

### 0.2

Stable Build

1. Added system which adds spaces to the message to bring it up to 9 charrects long.
2. docopt now working on the command line interface (i have left the arguments printing you can put a # infrot of line 83 ("print argument") if you wish to turn this off.
3. Removed the 0x infront of all the encodes.

### 0.1

Code uplaoded as it works in a basic state
1. Currently only works for 8 charecters
2. Currently does will only do A-Z,a-z,0-9 and some special's (anything between 0-127 in the ascii list
3. Added in docopt although its new to me a so trying to fix the problems
4. Currently encodes with 0x infront and need to remove that

## Special thanks

A big thanks to [/u/4144414D](https://github.com/4144414D) for all the help and showing me docops

Also a thanks to [docopt](http://docopt.org/) for the command line interface 
