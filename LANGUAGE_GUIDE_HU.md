# Geometry Dash - Nyelvváltás Funkció

## 🌐 Támogatott Nyelvek

- **English (EN)** 🇬🇧
- **Magyar (HU)** 🇭🇺

## 📋 Hogyan működik a nyelvváltás?

### Módszer 1: Beállítások Menü (Ajánlott)
1. Indítsd el a játékot
2. Kattints a **SETTINGS** (BEÁLLÍTÁSOK) gombra
3. A **LANGUAGE** (Nyelv) szekció alatt válaszd az **EN** vagy **HU** gombot
   - A kiválasztott gomb zöld színnel jelenik meg
4. A beállítás **automatikusan mentődik**
5. Az egész UI azonnal magyarra/angolra vált

### Módszer 2: Direkt Szerkesztés
Szerkeszd a `settings.json` fájlt:
```json
{
    "fullscreen": true,
    "music_volume": 0.5,
    "sfx_volume": 1.0,
    "skin_index": 1,
    "language": "hu"
}
```
Lehetséges értékek: `"en"` vagy `"hu"`

## ✨ Fordított Elemek

Az alábbi UI elemek támogatják a nyelvváltást:

- **Menü gombok**: PLAY, SETTINGS, MULTIPLAYER, UPDATE, EXIT
- **Beállítások**: SKIN, LANGUAGE, MUSIC VOLUME, SFX VOLUME, FULLSCREEN
- **Multiplayer**: HOST GAME, JOIN GAME, WAITING, CONNECTED
- **Játék**: Score, Speed, PAUSE, RESUME
- **Végeredmény**: GAME OVER, YOU WIN!, YOU LOSE!, NEW HIGH SCORE
- **Általános**: BACK, MENU, RESTART, CANCEL

## 🔄 Mik történik nyelvváltáskor?

1. Az UI azonnal frissül a kiválasztott nyelvre
2. A beállítás a `settings.json` fájlba kerül
3. Amikor újra indítod a játékot, az előző nyelvbeállítás betöltödik
4. Az összes szöveg angol fallback-kel rendelkezik, ha fordítás hiányzik

## 🛠️ Technikai Részletek

- **Translation File**: `translations.json` - 46+ fordítási kulcs
- **Fordítási Függvény**: `_t(key)` - lekéri a szöveget az aktuális nyelvhez
- **Default Nyelv**: English (en)
- **Encoding**: UTF-8

## 📝 Hozzáadás Saját Fordítások

Ha új szöveget szeretnél fordítani:

1. Nyisd meg a `translations.json` fájlt
2. Keress az `"en"` szekció alatt
3. Adj egy új kulcsot és angol szöveget:
```json
"MY_NEW_TEXT": "My English Text"
```

4. Majd a `"hu"` szekció alatt add meg a magyar fordítást:
```json
"MY_NEW_TEXT": "Az én magyar szövegem"
```

5. A kódban használd: `_t("MY_NEW_TEXT")`

## 🐛 Hibaelhárítás

**Probléma**: Az UI nem vált a kiválasztott nyelvre
- **Megoldás**: Indítsd újra a játékot

**Probléma**: Néhány szöveg még angolul jelenik meg
- **Megoldás**: Ez fallback, ha a fordítás hiányzik - jelezd az fejlesztőnek

**Probléma**: A beállítás nem mentődik
- **Megoldás**: Ellenőrizd, hogy a `settings.json` fájl írható-e

## 📧 Megjegyzések

- A nyelvváltás a beállítások menüből azonnal hat az UI-ra
- Az összes fordítás UTF-8 kódolással van mentve
- Új játék indításakor az utolsó kiválasztott nyelv betöltődik
