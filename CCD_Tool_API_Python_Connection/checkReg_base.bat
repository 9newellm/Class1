@echo off
setlocal

REM List of DLLs to check
set DLLs=SETUPAPI.DLL KERNEL32.DLL USER32.DLL OLE32.DLL SHELL32.DLL SHLWAPI.DLL

REM Registry key to search for registered DLLs
set REG_KEY=HKLM\SOFTWARE\Classes\CLSID

REM Loop through each DLL
for %%D in (%DLLs%) do (
    echo Checking registration for %%D...
    reg query %REG_KEY% /s /f "%%D" >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        echo %%D is registered.
    ) else (
        echo %%D is NOT registered.
    )
)

endlocal
pause
