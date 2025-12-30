"""Setup файл для установки пакета"""
from setuptools import setup, find_packages

setup(
    name="lawfulsiteparser",
    version="1.0.0",
    description="Парсер для сайтов судов",
    author="RomanLeva",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn[standard]>=0.24.0",
        "selenium>=4.15.2",
        "pytest>=7.4.3",
        "pytest-asyncio>=0.21.1",
        "httpx>=0.25.2",
    ],
    python_requires=">=3.8",
)



