#!/bin/bash

tmux kill-session -t djangoapi

# Start a tmux session with the name "djangoapi" or attach to it if it already exists
tmux new-session -d -s djangoapi || tmux attach -t djangoapi

# Send the commands to the tmux session
tmux send-keys -t djangoapi "source ~/djangoapi.combinator.de/venvlinux/bin/activate" C-m
tmux send-keys -t djangoapi "pip3.11 install -r  ~/djangoapi.combinator.de/requirements.txt" C-m
tmux send-keys -t djangoapi "cd ~/djangoapi.combinator.de/djangoapi/" C-m
tmux send-keys -t djangoapi "gunicorn djangoapi.wsgi" C-m
