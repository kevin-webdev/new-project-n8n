#!/bin/bash

# USAGE: ./generate_video.sh image.jpg voice.mp3 output.mp4

IMAGE="$1"
VOICE="$2"
OUTPUT="$3"

ffmpeg -y -loop 1 -i "$IMAGE" -i "$VOICE" \
  -c:v libx264 -c:a aac -shortest \
  -tune stillimage -pix_fmt yuv420p \
  -vf "scale=1080:1920,format=yuv420p" \
  "$OUTPUT"
