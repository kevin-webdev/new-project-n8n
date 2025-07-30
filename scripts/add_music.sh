#!/bin/bash

# USAGE: ./add_music.sh input.mp4 music.mp3 output.mp4

VIDEO="$1"
MUSIC="$2"
OUTPUT="$3"

ffmpeg -y -i "$VIDEO" -i "$MUSIC" -filter_complex \
  "[1:a]volume=0.2[a1];[0:a][a1]amix=inputs=2:duration=shortest" \
  -c:v copy -shortest "$OUTPUT"
