# Geometry Dash - Language Switching Feature

## 🌐 Supported Languages

- **English (EN)** 🇬🇧
- **Hungarian (HU)** 🇭🇺

## 📋 How Does Language Switching Work?

### Method 1: Settings Menu (Recommended)
1. Start the game
2. Click the **SETTINGS** button
3. In the **LANGUAGE** section, select **EN** or **HU**
   - The selected button will be highlighted in green
4. The setting **automatically saves**
5. The entire UI immediately switches to the selected language

### Method 2: Direct Editing
Edit the `settings.json` file:
```json
{
    "fullscreen": true,
    "music_volume": 0.5,
    "sfx_volume": 1.0,
    "skin_index": 1,
    "language": "en"
}
```
Possible values: `"en"` or `"hu"`

## ✨ Translated Elements

The following UI elements support language switching:

- **Menu buttons**: PLAY, SETTINGS, MULTIPLAYER, UPDATE, EXIT
- **Settings**: SKIN, LANGUAGE, MUSIC VOLUME, SFX VOLUME, FULLSCREEN
- **Multiplayer**: HOST GAME, JOIN GAME, WAITING, CONNECTED
- **Gameplay**: Score, Speed, PAUSE, RESUME
- **Results**: GAME OVER, YOU WIN!, YOU LOSE!, NEW HIGH SCORE
- **General**: BACK, MENU, RESTART, CANCEL

## 🔄 What Happens When You Switch Languages?

1. The UI instantly updates to the selected language
2. The setting is saved to the `settings.json` file
3. When you restart the game, the previous language preference is loaded
4. All text has English fallback if translation is missing

## 🛠️ Technical Details

- **Translation File**: `translations.json` - 46+ translation keys
- **Translation Function**: `_t(key)` - retrieves text for current language
- **Default Language**: English (en)
- **Encoding**: UTF-8

## 📝 Adding Your Own Translations

If you want to add new text translations:

1. Open the `translations.json` file
2. Find the `"en"` section
3. Add a new key and English text:
```json
"MY_NEW_TEXT": "My English Text"
```

4. Then in the `"hu"` section, add the Hungarian translation:
```json
"MY_NEW_TEXT": "Az én magyar szövegem"
```

5. In the code, use: `_t("MY_NEW_TEXT")`

## 🐛 Troubleshooting

**Issue**: The UI doesn't switch to the selected language
- **Solution**: Restart the game

**Issue**: Some text still appears in English
- **Solution**: This is a fallback if translation is missing - report to developers

**Issue**: The setting doesn't save
- **Solution**: Check that the `settings.json` file is writable

## 📧 Notes

- Language switching from the settings menu takes effect immediately on the UI
- All translations are saved with UTF-8 encoding
- The last selected language is loaded when you start a new game
- The system gracefully falls back to English for any missing translations
