@echo off
chcp 65001 >nul
title Geometry Dash PRO

echo.
echo =========================================
echo  Geometry Dash PRO - Indítás
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo HIBA: Python nincs telepítve vagy nincs az elérési útvonalban!
    echo.
    echo Telepítés: https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo Python verzió ellenőrzése... OK
echo.

REM Check if pygame is installed
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo HIBA: pygame nincs telepítve!
    echo.
    echo Telepítés: pip install pygame
    echo.
    pause
    exit /b 1
)

echo pygame modul ellenőrzése... OK
echo.
echo Játék indítása...
echo.

REM Run the game
python "%~dp0Geometry_Dash"

pause
