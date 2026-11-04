#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
echo "Cyber AI Lab: installing supported Termux packages"
pkg update
pkg install -y python git openssh curl nano nmap
mkdir -p "$HOME/cyber-ai-lab"
cp "$(dirname "$0")/lab.py" "$HOME/cyber-ai-lab/lab.py"
echo "Ready. Run: python ~/cyber-ai-lab/lab.py"
