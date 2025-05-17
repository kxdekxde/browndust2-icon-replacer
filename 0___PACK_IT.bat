@echo off
echo Running Python Scripts...



REM Run 4___bingle_kxde_repacker_LZ4_compressor.py
python 4___bingle_kxde_repacker_LZ4_compressor.py
if %errorlevel% neq 0 (
    echo 4___bingle_kxde_repacker_LZ4_compressor.py failed
    pause
    exit /b %errorlevel%
)
echo 4___bingle_kxde_repacker_LZ4_compressor.py ran successfully



REM Run 5___remove_bundle_extension.py
python 5___remove_bundle_extension.py
if %errorlevel% neq 0 (
    echo 5___remove_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 5___remove_bundle_extension.py ran successfully



echo All scripts ran successfully.
exit
