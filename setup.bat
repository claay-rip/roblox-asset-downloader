@echo off
title Library Installation

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [EN] Python is not installed or not added to PATH.
    echo [RU] Python ne ustanovlen ili ne dobavlen v PATH.
    echo.
    echo [EN] Please install Python and make sure to check "Add Python to PATH" during installation.
    echo [RU] Pozhaluysta ustanovite Python i otmet'te "Dobavit' Python v PATH" pri ustanovke.
    echo.
    echo [EN/RU] Download here: https://www.python.org/downloads/release/python-3120/
    echo.
    pause
    exit /b
)

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo [EN] Python is not installed or not added to PATH.
    echo [RU] Python ne ustanovlen ili ne dobavlen v PATH.
    echo.
    echo [EN/RU] Try reinstalling Python and make sure "Add Python to PATH" is selected.
    echo.
    pause
    exit /b
)

echo [EN] Installing required libraries...
echo [RU] Ustanovka neobkhodimykh bibliotek...
echo.
pip install -r requirements.txt
echo.

echo [EN] Installation complete!
echo [RU] Ustanovka zavershena!
echo.

echo [EN] Now open config.py in Notepad and configure it for your needs.
echo [RU] Teper' otkroyte config.py cherez bloknot i nastrojte ego pod sebya.
echo.
echo [EN/RU] GitHub: https://github.com/claay-rip/roblox-autojoiner
echo.

pause
