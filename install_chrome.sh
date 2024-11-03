# install_chrome.sh
#!/usr/bin/env bash
set -x

# Update package list and install Chromium
apt update && apt install -y chromium-browser
