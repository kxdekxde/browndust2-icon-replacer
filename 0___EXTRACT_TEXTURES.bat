@echo off
echo Running Python Scripts...



REM Run 1___rename_subfolders.py
python 1___rename_subfolders.py
if %errorlevel% neq 0 (
    echo 1___rename_subfolders.py failed
    pause
    exit /b %errorlevel%
)
echo 1___rename_subfolders.py ran successfully



REM Run 2___add_bundle_extension.py
python 2___add_bundle_extension.py
if %errorlevel% neq 0 (
    echo 2___add_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 2___add_bundle_extension.py ran successfully



REM Run 3___extract_textures.py
python 3___extract_textures.py
if %errorlevel% neq 0 (
    echo 3___extract_textures.py failed
    pause
    exit /b %errorlevel%
)
echo 3___extract_textures.py ran successfully




echo All scripts ran successfully.
exit
