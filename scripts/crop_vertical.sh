#!/bin/bash

# USAGE: ./crop_vertical.sh input.mp4 output.mp4

INPUT="$1"
OUTPUT="$2"

ffmpeg -y -i "$INPUT" -vf "crop=in_h*9/16:in_h:(in_w-out_w)/2:0" "$OUTPUT"
