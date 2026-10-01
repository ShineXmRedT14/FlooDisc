@echo off
cd /d "%~dp0"

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo Searching Python...
python --version >nul 2>&1

if errorlevel 1 (
    echo Python not found. Installing...
    winget install --id Python.Python.3.13 -e --source winget

    if errorlevel 1 (
        echo Failed to install Python.
        pause
        exit /b 1
    )
)

echo Python found.
python --version

echo Searching Npcap driver...
sc query npcap >nul 2>&1

if errorlevel 1 (
    echo Npcap driver not found. Installing...
    winget install --id Insecure.Npcap -e --source winget

    if errorlevel 1 (
        echo Failed to install Npcap driver.
        pause
        exit /b 1
    )
)

echo Npcap found.
sc query npcap

echo Creating virtual environment...
python -m venv .venv

echo Creating linker...
.venv\Scripts\python.exe -m pip install .

echo Creating global linker...
(
    echo @echo off
    echo "%~dp0.venv\Scripts\floodisc.exe" %%*
) > %WINDIR%\floodisc.bat

echo Successfully created global linker.
echo Clears build and .egg-info directories
rmdir /s /q build
rmdir /s /q floodisc.egg-info
pause