#!/usr/bin/env python3
"""
Geometry Dash PRO - Desktop Shortcut Creator
Létrehozza a parancsikont az asztalon
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def install_package(package_name):
    """Package telepítése pip-pel"""
    try:
        print(f"  → {package_name} telepítése...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name, "-q"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"  ✓ {package_name} sikeresen telepítve")
        return True
    except Exception as e:
        print(f"  ✗ {package_name} telepítése sikertelen: {e}")
        return False

def get_desktop_path():
    """Desktop mappa elérési útjának meghatározása"""
    # Először próbáljuk meg a hagyományos és OneDrive Desktop mappákat
    desktop_paths = [
        Path.home() / "OneDrive" / "Desktop",
        Path.home() / "OneDrive - Personal" / "Desktop",
        Path.home() / "Desktop",
    ]
    
    for desktop_path in desktop_paths:
        if desktop_path.exists():
            return desktop_path
    
    # Ha egyik sem létezik, hozz létre egyet
    default_desktop = Path.home() / "Desktop"
    default_desktop.mkdir(parents=True, exist_ok=True)
    return default_desktop

def create_shortcut():
    """Shortcut létrehozása az asztalra"""
    print("\n→ Parancsikon létrehozása...")
    
    # Először telepítjük a pywin32-t
    print("  → Szükséges csomagok telepítése...")
    install_package("pywin32")
    print()
    
    # Desktop elérési útjának meghatározása
    desktop_path = get_desktop_path()
    print(f"  Desktop mappa: {desktop_path}")
    print()
    
    # Próbáljuk meg a pywin32 verzióval (friss import után)
    try:
        # Force reimport
        import importlib
        if 'win32com' in sys.modules:
            del sys.modules['win32com']
        if 'win32com.client' in sys.modules:
            del sys.modules['win32com.client']
        
        from win32com.client import Dispatch
        
        script_dir = Path(__file__).parent
        shortcut_path = desktop_path / "Geometry Dash PRO.lnk"
        
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = sys.executable
        shortcut.Arguments = f'"{script_dir / "run.py"}"'
        shortcut.WorkingDirectory = str(script_dir)
        shortcut.Description = "Geometry Dash PRO - Game Launcher"
        shortcut.save()
        
        print("✓ Parancsikon sikeresen létrehozva az asztalon!")
        print(f"  Fájl: {shortcut_path}")
        return True
        
    except Exception as e:
        print(f"⚠ .lnk parancsikon létrehozása nem működött: {e}")
        print("  → Fallback: Python launcher fájl létrehozása...")
        
        # Fallback: Python launcher (.pyw fájl az asztalon)
        try:
            script_dir = Path(__file__).parent
            launcher_path = desktop_path / "Geometry Dash PRO.pyw"
            
            launcher_content = f"""#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

script_dir = Path(r"{script_dir}")
run_py = script_dir / "run.py"

if __name__ == "__main__":
    subprocess.run([sys.executable, str(run_py)], cwd=str(script_dir))
"""
            
            with open(launcher_path, 'w', encoding='utf-8') as f:
                f.write(launcher_content)
            
            print("✓ Python launcher sikeresen létrehozva az asztalon!")
            print(f"  Fájl: {launcher_path}")
            print("  Megjegyzés: Ez a .pyw fájl Python scriptet futtat közvetlenül")
            return True
            
        except Exception as e2:
            print(f"✗ Fallback is sikertelen: {e2}")
            print(f"  Desktop elérési út: {desktop_path}")
            print(f"  A mappában való írás nem lehetséges (OneDrive szinkronizáció?)")
            return False

def check_python():
    """Python telepítés és modulok ellenőrzése"""
    try:
        import pygame
        print("✓ Python és pygame modul OK")
        return True
    except ImportError:
        print("✗ pygame nincs telepítve")
        print("  → pygame telepítése...")
        if install_package("pygame"):
            print("✓ pygame sikeresen telepítve")
            return True
        else:
            print("✗ pygame telepítése sikertelen")
            return False

if __name__ == "__main__":
    print("=" * 60)
    print("  Geometry Dash PRO - Telepítő")
    print("=" * 60)
    print()
    
    # Python ellenőrzése
    print("1. Python és modulok ellenőrzése...")
    if not check_python():
        print("\n" + "=" * 60)
        print("✗ Telepítés sikertelen")
        print("=" * 60)
        input("\nNyomj egy gombot a kilépéshez...")
        sys.exit(1)
    print()
    
    # Parancsikon létrehozása
    print("2. Desktop parancsikon létrehozása...")
    shortcut_created = create_shortcut()
    print()
    
    print("=" * 60)
    print("✓ Telepítés befejezve!")
    print("=" * 60)
    print("\n📌 Következő lépések:")
    if shortcut_created:
        print("   ✓ Desktop parancsikon elérhető: 'Geometry Dash PRO'")
        print("   • Dupla kattintás az asztalon a játék indításához")
    else:
        print("   • Parancsikon létrehozása sikertelen volt")
    print("   • Vagy futtasd közvetlen: python run.py")
    print()
