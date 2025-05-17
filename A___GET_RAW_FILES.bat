@echo off
echo Running Python Scripts...


REM Run B___copy_backup_to_moddedbundles.py
python B___copy_backup_to_moddedbundles.py
if %errorlevel% neq 0 (
    echo B___copy_backup_to_moddedbundles.py failed
    pause
    exit /b %errorlevel%
)
echo B___copy_backup_to_moddedbundles.py ran successfully



REM Run C___copy_raw_data_files.py
python C___copy_raw_data_files.py
if %errorlevel% neq 0 (
    echo C___copy_raw_data_files.py failed
    pause
    exit /b %errorlevel%
)
echo C___copy_raw_data_files.py ran successfully



echo All scripts ran successfully.
exit
