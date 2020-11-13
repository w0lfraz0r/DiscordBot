#!/bin/sh

TIMEOUT="5s"
while : ; do
  python main.py
  echo "Retarting in $TIMEOUT"
  sleep $TIMEOUT
done