# Решение проблем с драйверами браузеров

## Проблема: "Unable to obtain driver for MicrosoftEdge using Selenium Manager"

Эта ошибка возникает, когда Selenium не может автоматически скачать драйвер браузера из-за проблем с интернетом или DNS.

## Решения

### Решение 1: Использовать Chrome (если установлен)

```powershell
# Остановите текущее приложение (Ctrl+C)
# Затем запустите с Chrome:
cd "C:\Users\kam1k88\Desktop\lawfulsiteparser_python"
.\venv\Scripts\Activate.ps1
$env:BROWSER_TYPE="chrome"
$env:HEADLESS_MODE="false"
python main.py
```

### Решение 2: Скачать EdgeDriver вручную

1. **Узнайте версию Edge:**
   - Откройте Edge
   - Перейдите в `edge://version/`
   - Запомните номер версии (например, 120.0.2210.91)

2. **Скачайте EdgeDriver:**
   - Перейдите на: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - Или используйте: https://msedgedriver.azureedge.net/
   - Скачайте версию, соответствующую вашему Edge
   - Распакуйте `msedgedriver.exe`

3. **Укажите путь к драйверу:**
   ```powershell
   # Положите msedgedriver.exe в папку проекта или в PATH
   # Затем установите переменную:
   $env:EDGE_DRIVER_PATH="C:\Users\kam1k88\Desktop\lawfulsiteparser_python\msedgedriver.exe"
   $env:BROWSER_TYPE="edge"
   python main.py
   ```

### Решение 3: Использовать webdriver-manager (автоматическое управление)

Установите webdriver-manager:
```powershell
pip install webdriver-manager
```

Затем измените `src/lawfulsiteparser/parser/parser.py`:
```python
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

# В конструкторе:
if browser == "edge":
    service = Service(EdgeChromiumDriverManager().install())
    self.driver = webdriver.Edge(service=service, options=options)
```

### Решение 4: Использовать системный EdgeDriver (если установлен)

Если EdgeDriver уже установлен в системе:
```powershell
# Проверьте, есть ли в PATH:
where.exe msedgedriver

# Если есть, просто используйте:
$env:BROWSER_TYPE="edge"
python main.py
```

## Проверка работы

После применения решения проверьте:
1. http://localhost:8000/parser/ping - должно работать
2. http://localhost:8000/parser/start_parser - должно инициализировать парсер

## Текущая конфигурация

Проверьте текущие настройки:
```powershell
Write-Host "BROWSER_TYPE: $env:BROWSER_TYPE"
Write-Host "HEADLESS_MODE: $env:HEADLESS_MODE"
Write-Host "EDGE_DRIVER_PATH: $env:EDGE_DRIVER_PATH"
Write-Host "CHROME_DRIVER_PATH: $env:CHROME_DRIVER_PATH"
```



