#!/usr/bin/env python3
"""
Geometry Dash PRO - Desktop Shortcut Creator
Létrehozza a parancsikont az asztalon
"""

import os
import sys
import json
from pathlib import Path

def create_shortcut():
    """Shortcut létrehozása az asztalra"""
    try:
        # Windows shortcut library
        from win32com.client import Dispatch
        
        # Elérési útvonalak
        script_dir = Path(__file__).parent
        desktop_path = Path.home() / "Desktop"
        game_path = script_dir / "Geometry_Dash"
        
        # Shortcut fájl elérési útja
        shortcut_path = desktop_path / "Geometry Dash PRO.lnk"
        
        # Shortcut létrehozása
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = str(game_path)
        shortcut.WorkingDirectory = str(script_dir)
        shortcut.Description = "Geometry Dash PRO"
        shortcut.save()
        
        print("\n✓ Parancsikon sikeresen létrehozva az asztalon!")
        print(f"  Elérési út: {shortcut_path}")
        return True
        
    except ImportError:
        print("\n⚠ ERROR: A win32com package nincs telepítve.")
        print("  Telepítés: pip install pywin32")
        return False
    except Exception as e:
        print(f"\n✗ HIBA: A parancsikon létrehozása sikertelen!\n  {str(e)}")
        return False

def check_python():
    """Python telepítés ellenőrzése"""
    try:
        import pygame
        print("✓ Python 3 és szükséges modulok OK")
        return True
    except ImportError:
        print("✗ HIBA: pygame nincs telepítve!")
        print("  Telepítés: pip install pygame")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("  Geometry Dash PRO - Telepítő")
    print("=" * 50)
    print()
    
    # Python ellenőrzése
    print("1. Python ellenőrzése...")
    if not check_python():
        print("\nTelependítés szükséges!")
        sys.exit(1)
    
    print("\n2. Parancsikon létrehozása...")
    if create_shortcut():
        print("\n" + "=" * 50)
        print("✓ Telepítés sikeres!")
        print("=" * 50)
        print("\nA játék elérhető az asztalon: 'Geometry Dash PRO'")
    else:
        print("\n" + "=" * 50)
        print("✗ Telepítés részben sikertelen")
        print("=" * 50)
        sys.exit(1)
