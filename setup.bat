@echo off
chcp 65001 >nul
title Geometry Dash PRO - Telepítés

echo.
echo =========================================
echo  Geometry Dash PRO - Telepítés
echo =========================================
echo.
echo Parancsikon létrehozása az asztalon...
echo.

REM Run the VBScript to create the shortcut
cscript.exe "%~dp0create_shortcut.vbs"

if %errorlevel% equ 0 (
    echo.
    echo =========================================
    echo  Telepítés sikeres!
    echo =========================================
    echo.
    echo Parancsikon letöltve az asztalra.
    echo Játék indítása: kétszer kattints az asztalon lévő "Geometry Dash PRO" ikonra
    echo.
    timeout /t 3
) else (
    echo.
    echo  HIBA: A telepítés sikertelen!
    echo.
    timeout /t 5
)
