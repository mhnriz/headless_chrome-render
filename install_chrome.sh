# install_chrome.sh
#!/usr/bin/env bash
set -x
CHROME_PATH="/usr/bin/google-chrome"
if [ ! -f "$CHROME_PATH" ]; then
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    apt update && apt install -y ./google-chrome-stable_current_amd64.deb
    rm google-chrome-stable_current_amd64.deb
fi
