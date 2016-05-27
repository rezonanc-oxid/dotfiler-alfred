#!/bin/bash

cat "$1" | $HOME/homebrew/bin/fzf -f "$2" | $HOME/bin/alfred/alfred_items_simple.py
