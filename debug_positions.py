#!/usr/bin/env python3
"""
Debug script a beállítások menü Y-pozícióinak ellenőrzésére
"""

print("Event Handler Y-pozíciók:")
print("=" * 50)

# Event handler részben
skin_y_event = 145
lang_y_event = 235
fullscreen_y_event = 505

print(f"Szkin gombok Y:       {skin_y_event}")
print(f"Language gombok Y:    {lang_y_event}")
print(f"Fullscreen gomb Y:    {fullscreen_y_event}")

print("\n" + "=" * 50)
print("Rajzolás részben (kalkulált Y-értékek):")
print("=" * 50)

# Rajzolás részben
y_pos = 130

# Szkin
skin_y_draw = y_pos + 15
print(f"1. y_pos = {y_pos}")
print(f"   Szkin gombok Y: {y_pos} + 15 = {skin_y_draw}")

y_pos += 90

# Language
lang_y_draw = y_pos + 15
print(f"2. y_pos += 90 = {y_pos}")
print(f"   Language gombok Y: {y_pos} + 15 = {lang_y_draw}")

y_pos += 90

# Music
print(f"3. y_pos += 90 = {y_pos}")
print(f"   (Music sliders)")

y_pos += 90

# SFX
print(f"4. y_pos += 90 = {y_pos}")
print(f"   (SFX sliders)")

y_pos += 90

# Fullscreen
fullscreen_y_draw = y_pos + 15
print(f"5. y_pos += 90 = {y_pos}")
print(f"   Fullscreen gomb Y: {y_pos} + 15 = {fullscreen_y_draw}")

print("\n" + "=" * 50)
print("SZINKRONIZÁCIÓ ELLENŐRZÉS:")
print("=" * 50)

if skin_y_event == skin_y_draw:
    print(f"✓ Szkin: Event={skin_y_event} Draw={skin_y_draw} - MATCH")
else:
    print(f"✗ Szkin: Event={skin_y_event} Draw={skin_y_draw} - MISMATCH")

if lang_y_event == lang_y_draw:
    print(f"✓ Language: Event={lang_y_event} Draw={lang_y_draw} - MATCH")
else:
    print(f"✗ Language: Event={lang_y_event} Draw={lang_y_draw} - MISMATCH")

if fullscreen_y_event == fullscreen_y_draw:
    print(f"✓ Fullscreen: Event={fullscreen_y_event} Draw={fullscreen_y_draw} - MATCH")
else:
    print(f"✗ Fullscreen: Event={fullscreen_y_event} Draw={fullscreen_y_draw} - MISMATCH")

print("=" * 50)
