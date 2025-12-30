# Быстрый старт

## Быстрая установка и запуск

1. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

2. **Выберите браузер (опционально):**
   - **Edge (по умолчанию на Windows)**: Работает автоматически, ничего устанавливать не нужно!
   - **Chrome**: Если хотите использовать Chrome, установите ChromeDriver и установите `$env:BROWSER_TYPE="chrome"`

3. **Запустите приложение:**
```bash
python main.py
```

4. **Проверьте работу:**
   - Откройте браузер: http://localhost:8000/docs
   - Проверьте ping: http://localhost:8000/parser/ping

## Запуск тестов

```bash
# Все тесты
pytest

# Конкретный тест
pytest tests/test_application.py::test_ping_endpoint

# С подробным выводом
pytest -v
```

## Переменные окружения

Можно настроить через переменные окружения:

```powershell
# Windows PowerShell
$env:MOSGORSUD_URL="https://mos-gorsud.ru"
$env:BROWSER_TYPE="edge"  # или "chrome"
$env:HEADLESS_MODE="false"  # false для видимого браузера, true для headless
# Опционально, если нужен ручной путь к драйверу:
# $env:EDGE_DRIVER_PATH="C:\path\to\msedgedriver.exe"
# $env:CHROME_DRIVER_PATH="C:\path\to\chromedriver.exe"

# Linux/Mac
export MOSGORSUD_URL="https://mos-gorsud.ru"
export BROWSER_TYPE="chrome"  # или "edge"
export HEADLESS_MODE="true"
# Опционально:
# export CHROME_DRIVER_PATH="/usr/local/bin/chromedriver"
# export EDGE_DRIVER_PATH="/usr/local/bin/msedgedriver"
```

## Структура проекта

- `main.py` - точка входа приложения
- `config/config.py` - настройки
- `src/lawfulsiteparser/` - основной код
- `tests/` - тесты
- `requirements.txt` - зависимости

