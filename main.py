"""Главный файл приложения"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.lawfulsiteparser.controller.parser_controller import router as parser_router
from src.lawfulsiteparser.parser.parser import Parser
from src.lawfulsiteparser.service.parser_service import ParserService
from src.lawfulsiteparser.aspect.exception_handler import (
    illegal_state_exception_handler,
    playwright_timeout_exception_handler,
    parser_exception_handler,
    general_exception_handler,
    IllegalStateError
)
from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from src.lawfulsiteparser.aspect.exception.parser_exception import ParserException

# Глобальные переменные для зависимостей
parser_instance: Parser = None
parser_service_instance: ParserService = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения"""
    global parser_instance, parser_service_instance
    
    # Инициализация отложена до первого использования
    # Это позволяет приложению запуститься даже если браузер недоступен
    parser_instance = None
    parser_service_instance = None
    
    yield
    
    # Очистка при завершении
    if parser_instance:
        import asyncio
        try:
            asyncio.run(parser_instance.close())
        except Exception:
            pass


app = FastAPI(
    title="LawfulSiteParser",
    description="Парсер для сайтов судов",
    version="1.0.0",
    lifespan=lifespan
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация обработчиков исключений
app.add_exception_handler(IllegalStateError, illegal_state_exception_handler)
app.add_exception_handler(PlaywrightTimeoutError, playwright_timeout_exception_handler)
app.add_exception_handler(ParserException, parser_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Регистрация роутеров
app.include_router(parser_router)


# Экспортируем функцию для использования в контроллере
__all__ = ['app', 'parser_service_instance']


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

