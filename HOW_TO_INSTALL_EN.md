# Geometry Dash PRO - Installation Guide

## ⚡ Quick Start (30 seconds)

1. Extract the files
2. Double-click: **`setup.py`**
3. Shortcut appears on your Desktop
4. Start playing! 🎮

---

## 📋 Detailed Installation

### 1. Check Prerequisites

#### Python 3.9+ is required

**On Windows:**
```bash
python --version
```

If not installed:
- Download from: https://www.python.org/downloads/
- During installation **check**: "Add Python to PATH"

---

### 2. Download Project

#### From GitHub:
1. Click: **Code → Download ZIP**
2. Extract to a folder of your choice
3. Open the folder

---

### 3. Automatic Installation (Recommended)

#### Option A: Python Script
```bash
python setup.py
```

#### Option B: Direct Game Launch
```bash
python run.py
```

---

### 4. Manual Installation (If automatic fails)

#### 4.1. Install pygame
```bash
pip install pygame
```

#### 4.2. Create Shortcut (optional)
```bash
python setup.py
```

#### 4.3. Launch Game
```bash
python run.py
```

---

## 🎮 Starting the Game

### From Desktop (after setup):
- Double-click: **"Geometry Dash PRO"** shortcut

### From Command Prompt:
```bash
python run.py
```

---

## ⚙️ Settings

Available in-game:
- **20 Color Skins** - Choose your favorite color!
- **Volume Settings** - Control music and SFX separately
- **Fullscreen Mode** - Play in fullscreen
- **Multiplayer Mode** - Play online with friends

---

## 🐛 Troubleshooting

### "Python is not installed"
```bash
# Download: https://www.python.org/
# During installation check: "Add Python to PATH"
```

### "pygame module is missing"
```bash
pip install pygame
```

### "Shortcut was not created"
1. Open Command Prompt as **Administrator**
2. Run: `python setup.py`

### Game won't start
1. Check Python version: `python --version` (3.9+)
2. Reinstall pygame: `pip install --upgrade pygame`

---

## 📁 Folder Structure

```
Geometry-Dash/
├── Geometry_Dash          # Main game file
├── setup.py               # Automatic installer (Python)
├── run.py                 # Game launcher
├── background.mp3         # Game music
├── menumusic.mp3          # Menu music
├── scores.json            # High scores
├── settings.json          # Settings
└── README.md              # Project description
```

---

## ❓ More Questions?

**Multiplayer on Game Server:**
- Host: Create a room
- Client: Join using IP

**Save Skins:** Automatic in Settings menu

**Save Scores:** Automatic after first game

---

## 🎉 You're Ready!

Enjoy the game! 🚀

```
Geometry Dash PRO v1.0
Windows 10/11 Compatible
```
