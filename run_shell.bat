@echo off
REM Simple Python Shell Launcher
REM This batch file checks if Python is installed and runs the shell

echo Launching Simple Python Shell...

REM Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python not found! Please install Python and try again.
    pause
    exit /b 1
)

REM Run the shell
python "%~dp0simple_shell.py"