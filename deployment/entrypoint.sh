#!/bin/bash
set -e

# Change the ownership of the /var/lib/langflow directory
chown -R 1000:1000 /var/lib/langflow

# Execute the main process
exec "$@"

