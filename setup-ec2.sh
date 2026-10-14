#!/bin/bash
# Run this once on a fresh Ubuntu EC2 instance.
# It installs Docker and Git.

set -e

sudo apt update
sudo apt install -y docker.io git
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu

echo "Done. Log out and log back in so Docker works without sudo."
