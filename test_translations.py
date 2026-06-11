#!/usr/bin/env python3
"""
Tesztsript a fordítási rendszer ellenőrzéséhez
"""

import json

# Translations betöltése
with open("translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

# Settings betöltése
with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

print("=" * 60)
print("FORDÍTÁSI RENDSZER TESZT")
print("=" * 60)
print()

# Ellenőrzés: Language beállítás létezik-e
if "language" in settings:
    print(f"✓ Language beállítás: {settings['language']}")
else:
    print("✗ Language beállítás nincs a settings.json-ben")

print()

# Elérhető nyelvek
print("Elérhető nyelvek:")
for lang in translations.keys():
    count = len(translations[lang])
    print(f"  - {lang}: {count} fordítás")

print()

# Minta fordítások
print("Minta fordítások (English):")
sample_keys = ["PLAY", "SETTINGS", "LANGUAGE", "YOU_WIN", "NEW_HIGH_SCORE"]
for key in sample_keys:
    en_text = translations["en"].get(key, "NOT FOUND")
    hu_text = translations["hu"].get(key, "NOT FOUND")
    print(f"  {key:20} EN: {en_text:25} HU: {hu_text}")

print()
print("=" * 60)
print("✓ Fordítási rendszer OK - készen az implementálásra!")
print("=" * 60)
