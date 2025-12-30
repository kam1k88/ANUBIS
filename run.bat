@echo off
REM Переходим в папку проекта
cd /d "%~dp0"

REM Настройки окружения (можно не трогать)
set MOSGORSUD_URL=https://mos-gorsud.ru
set BROWSER_TYPE=chromium
set HEADLESS_MODE=true

REM Запуск приложения
python main.py

pause
