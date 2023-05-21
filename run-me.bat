@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
set "errors="

echo "Checking Python installation..."
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo "Python is not installed. Attempting to install Python..."
    echo.
    start https://www.python.org/downloads/
    echo "After installation, please run this script again."
    pause
    exit /b
)

echo "Checking pip installation..."
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo "Pip (Python package installer) is not installed. Attempting to install Pip..."
    echo.
    powershell -Command "& { iwr https://bootstrap.pypa.io/get-pip.py -o get-pip.py }" >nul 2>&1
    python get-pip.py >nul 2>&1
    DEL get-pip.py
)

echo "Checking required Python packages..."
set packages=subprocess whois datetime itertools requests rich time
for %%i in (%packages%) do (
    python -c "import %%i" >nul 2>&1
    if errorlevel 1 (
        echo.
        echo "Python package %%i is not installed. Attempting to install %%i..."
        echo.
        python -m pip install %%i >nul 2>&1
        if errorlevel 1 (
            echo "Couldn't install package %%i. Please ensure you have internet connection and sufficient privileges."
            if defined errors (
                set "errors=!errors! %%i"
            ) else (
                set "errors=%%i"
            )
        )
    )
)

if defined errors (
    echo.
    echo "Some packages (%errors%) could not be installed. Please try again or install them manually."
    pause
    exit /b
)

start cmd.exe /k python DomainWizard.py
