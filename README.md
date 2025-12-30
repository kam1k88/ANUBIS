# LawfulSiteParser

Парсер для сайтов судов (МосГорСуд) на Python с использованием Playwright и FastAPI.

## Описание

Проект представляет собой веб-приложение для парсинга данных с сайта МосГорСуд. Приложение предоставляет REST API для запуска парсера и автоматизированного сбора информации о судебных делах.

## Структура проекта

```
lawfulsiteparser_python/
├── config/
│   └── config.py              # Конфигурация приложения
├── src/
│   └── lawfulsiteparser/
│       ├── parser/
│       │   └── parser.py       # Основной класс парсера
│       ├── service/
│       │   └── parser_service.py  # Сервис для управления парсером
│       ├── controller/
│       │   └── parser_controller.py  # REST API контроллер
│       └── aspect/
│           ├── exception_handler.py  # Обработчик исключений
│           └── exception/
│               └── parser_exception.py  # Исключения парсера
├── tests/
│   ├── test_parser_algorithm.py  # Тесты алгоритма парсера
│   └── test_application.py       # Тесты приложения
├── main.py                    # Главный файл приложения
├── requirements.txt           # Зависимости проекта
└── README.md                  # Документация
```

## Установка

1. Установите Python 3.8 или выше

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Установите браузеры Playwright:
```bash
playwright install chromium
```
   - Playwright автоматически скачивает и управляет браузерами
   - Не требуется установка драйверов вручную!
   - Для Edge на Windows используется Chromium (совместим с Edge)

4. (Опционально) Установите пакет в режиме разработки:
```bash
pip install -e .
```

## Настройка

Настройки можно изменить в файле `config/config.py` или через переменные окружения:

- `MOSGORSUD_URL` - URL сайта для парсинга (по умолчанию: https://mos-gorsud.ru)
- `BROWSER_TYPE` - тип браузера: "chromium", "firefox" или "webkit" (по умолчанию: "chromium")
- `HEADLESS_MODE` - запуск браузера в headless режиме (по умолчанию: true)
- `TIMEOUT` - таймаут ожидания в миллисекундах (по умолчанию: 30000)

### Выбор браузера

**Chromium (по умолчанию, рекомендуется):**
- Автоматически устанавливается через `playwright install chromium`
- На Windows использует Chromium, совместимый с Edge
- Не требует дополнительной настройки

**Firefox:**
```bash
playwright install firefox
$env:BROWSER_TYPE="firefox"
```

**WebKit (Safari):**
```bash
playwright install webkit
$env:BROWSER_TYPE="webkit"
```

Для выбора браузера установите переменную окружения:
```powershell
# Для Chromium (по умолчанию)
$env:BROWSER_TYPE="chromium"

# Для Firefox
$env:BROWSER_TYPE="firefox"

# Для WebKit
$env:BROWSER_TYPE="webkit"
```

## Запуск

### Запуск приложения

```bash
python main.py
```

Или с помощью uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Приложение будет доступно по адресу: http://localhost:8000

### API Endpoints

- `GET /parser/ping` - Проверка работоспособности приложения
- `GET /parser/start_parser` - Запуск парсера

### Документация API

После запуска приложения документация доступна по адресу:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Тестирование

Запуск тестов:

```bash
pytest tests/
```

Запуск конкретного теста:

```bash
pytest tests/test_parser_algorithm.py::test_site_loading
```

## Особенности

- Использование Playwright для автоматизации браузера (современная альтернатива Selenium)
- Автоматическая установка и управление браузерами
- REST API на FastAPI
- Асинхронная работа (async/await)
- Обработка исключений
- Автоматические тесты на pytest
- Поддержка headless режима браузера
- Автоматическое создание директории для загрузок

## Преимущества Playwright

- ✅ Автоматическая установка браузеров - не нужно скачивать драйверы вручную
- ✅ Современный API с async/await
- ✅ Лучшая производительность и стабильность
- ✅ Встроенная поддержка всех браузеров
- ✅ Автоматическое ожидание элементов
- ✅ Отличная поддержка Edge/Chromium на Windows

## Миграция с Java

Проект был рефакторен с Java (Spring Boot) на Python (FastAPI). Основные изменения:

- Spring Boot → FastAPI
- JUnit → pytest
- Java Selenium → Python Playwright
- Maven/Gradle → pip/requirements.txt

## Лицензия

Проект создан для образовательных целей.

