#!/bin/sh

# Keep the container running
tail -f /dev/null &

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Start the Python server
exec python server.py
