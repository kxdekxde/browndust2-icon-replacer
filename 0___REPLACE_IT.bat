@echo off
echo Running Python Scripts...



REM Run 6___replace_file.py
python 6___replace_file.py
if %errorlevel% neq 0 (
    echo 6___replace_file.py failed
    pause
    exit /b %errorlevel%
)
echo 6___replace_file.py ran successfully


REM Run 7___clean_folders.py
python 7___clean_folders.py
if %errorlevel% neq 0 (
    echo 7___clean_folders.py failed
    pause
    exit /b %errorlevel%
)
echo 7___clean_folders.py ran successfully



echo All scripts ran successfully.
exit
