@echo off
echo Requesting Administrator privileges...
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Success: Administrator privileges confirmed.
) else (
    echo Failure: Current permissions inadequate.
    echo Please right-click this file and select "Run as Administrator".
    pause
    exit
)

echo.
echo Adding "127.0.0.1 Agric_Advisor" to hosts file...
findstr /C:"127.0.0.1 Agric_Advisor" "%WINDIR%\System32\drivers\etc\hosts" >nul
if %errorLevel% == 0 (
    echo Entry already exists.
) else (
    echo 127.0.0.1 Agric_Advisor >> "%WINDIR%\System32\drivers\etc\hosts"
    echo Entry added successfully.
)

echo.
echo You can now access the app at: http://Agric_Advisor:5000
echo (Make sure the Flask app is running)
echo.
pause
