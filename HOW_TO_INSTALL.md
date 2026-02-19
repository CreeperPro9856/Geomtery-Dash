# Geometry Dash PRO - Telepítési Útmutató

## ⚡ Gyorstipp (30 másodperc)

1. Nzip-ed ki a fájlokat
2. Dupla kattintás: **`setup.bat`**
3. Parancsikon megjelenik az asztalon
4. Játék indítása! 🎮

---

## 📋 Részletes Telepítés

### 1. Előfeltételek Ellenőrzése

#### Python 3.9+ szükséges

**Windows-on:**
```bash
python --version
```

Ha nem telepítve van:
- Töltsd le: https://www.python.org/downloads/
- Telepítés közben **jelöld be**: "Add Python to PATH"

---

### 2. Projekt Letöltése

#### GitHub-ról:
1. Kattints: **Code → Download ZIP**
2. Csomagold ki tetszőleges helyre
3. Nyiss meg a mappát

---

### 3. Automata Telepítés (Ajánlott)

#### Lehetőség A: Batch file
```bash
# Dupla kattintás a setup.bat fájlra
# VAGY parancssorban:
setup.bat
```

#### Lehetőség B: Python script
```bash
python setup.py
```

#### Lehetőség C: Játék közvetlen indítása
```bash
# Dupla kattintás a run.bat fájlra
# VAGY parancssorban:
run.bat
```

---

### 4. Manuális Telepítés (Ha az automata nem működik)

#### 4.1. pygame Telepítése
```bash
pip install pygame
```

#### 4.2. Parancsikon Létrehozása (opcionális)
```bash
python setup.py
```

#### 4.3. Játék Indítása
```bash
python Geometry_Dash
```

---

## 🎮 Játék Indítása

### Az asztalon (Setup után):
- Dupla kattintás: **"Geometry Dash PRO"** parancsikon

### Parancssorból:
```bash
python Geometry_Dash
```

### Batch file-ből:
- Dupla kattintás: **`run.bat`**

---

## ⚙️ Beállítások

A játékban elérhető:
- **20 szín skin** - Válassz a kedvenc színedből!
- **Hangerő beállítások** - Zenét és SFX-et külön szabályozd
- **Fullscreen mód** - Teljes képernyős játék
- **Multiplayer üzemmód** - Játssz online barátaiddal

---

## 🐛 Hibaelhárítás

### "Python nincs telepítve"
```bash
# Letöltés: https://www.python.org/
# Telepítés közben jelöld be: "Add Python to PATH"
```

### "pygame modul hiányzik"
```bash
pip install pygame
```

### "Parancsikon nem jött létre"
1. Nyiss parancsort mint **Rendszergazda**
2. Futtasd: `python setup.py`

### A játék nem indul
1. Ellenőrizd a Python verzióját: `python --version` (3.9+)
2. Telepítsd újra a pygame-t: `pip install --upgrade pygame`

---

## 📁 Mappaszerkezet

```
Geometry-Dash/
├── Geometry_Dash          # Fő játék fájl
├── setup.bat              # Automata telepítő (Windows)
├── setup.py               # Automata telepítő (Python)
├── run.bat                # Játék indító
├── create_shortcut.vbs    # VBScript parancsikon létrehozáshoz
├── background.mp3         # Játék zene
├── menumusic.mp3          # Menü zene
├── scores.json            # Magas pontok
├── settings.json          # Beállítások
└── README.md              # Projekt leírása
```

---

## ❓ További Kérdések?

**Játék szerverén futó multiplayer:**
- Host: Hozd létre a szobát
- Client: Csatlakozz az IP-hez

**Skinok mentése:** Automatikus a Settings menüben

**Pontok lementése:** Automata az első játék után

---

## 🎉 Kész!

Élvezd a játékot! 🚀

```
Geometry Dash PRO v1.0
Windows 10/11 kompatiblis

