#!/bin/bash
# Quick start shell script

echo "🚀 AI Media Generator - Quick Start"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed"
    exit 1
fi

# Run Python quickstart
python3 quickstart.py

# Ask if user wants to continue with setup
echo ""
read -p "Do you want to run setup? (Y/N): " choice
case "$choice" in 
    [Yy]* ) bash setup.sh;;
    [Nn]* ) 
        echo ""
        echo "To run the setup later, execute: bash setup.sh"
        echo "To start the server, execute: python3 main.py"
        ;;
esac
