#!/usr/bin/env python3
"""
Geometry Dash PRO - Game Launcher
Elindítja a Geometry Dash játékot
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Python verzió ellenőrzése"""
    if sys.version_info < (3, 6):
        print("✗ HIBA: Python 3.6+ szükséges!")
        print(f"  Aktuális verzió: {sys.version}")
        return False
    return True

def check_pygame():
    """pygame modul ellenőrzése"""
    try:
        import pygame
        print("✓ pygame modul OK")
        return True
    except ImportError:
        print("✗ HIBA: pygame nincs telepítve!")
        print("  Telepítés: pip install pygame")
        print("\n  Próbáld futtatni a setup.py fájlt először!")
        return False

def run_game():
    """Játék futtatása"""
    try:
        script_dir = Path(__file__).parent
        game_path = script_dir / "Geometry_Dash"
        
        print("Játék indítása...")
        print()
        
        # Futtatjuk a Geometry_Dash mappában lévő main fájlt
        result = subprocess.run(
            [sys.executable, str(game_path)],
            cwd=str(script_dir),
            check=False
        )
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"✗ HIBA: A játék futtatása sikertelen!\n  {str(e)}")
        return False

def main():
    """Főprogram"""
    print("=" * 60)
    print("  Geometry Dash PRO - Indítás")
    print("=" * 60)
    print()
    
    # Python verzió ellenőrzése
    print("1. Python verzió ellenőrzése...")
    if not check_python_version():
        print("\nTelependítés: https://www.python.org/")
        input("\nNyomj egy gombot a kilépéshez...")
        sys.exit(1)
    print(f"  OK - Python {sys.version.split()[0]}")
    print()
    
    # pygame ellenőrzése
    print("2. pygame modul ellenőrzése...")
    if not check_pygame():
        input("\nNyomj egy gombot a kilépéshez...")
        sys.exit(1)
    print()
    
    # Játék futtatása
    print("3. Játék indítása...")
    print()
    
    if run_game():
        print("\n✓ Játék leállt normálisan")
    else:
        print("\n⚠ A játék hibával zárult")
        input("Nyomj egy gombot a kilépéshez...")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Játék leállítva felhasználóval")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Váratlan hiba: {str(e)}")
        input("Nyomj egy gombot a kilépéshez...")
        sys.exit(1)
