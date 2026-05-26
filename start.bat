@echo off
REM Quick start batch file

echo AI Media Generator - Quick Start
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Run Python quickstart
python quickstart.py

REM Ask if user wants to continue with setup
echo.
set /p choice="Do you want to run setup? (Y/N): "
if /i "%choice%"=="Y" (
    call setup.bat
) else (
    echo.
    echo To run the setup later, execute: setup.bat
    echo To start the server, execute: python main.py
    pause
)
