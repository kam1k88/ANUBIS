import asyncio
from src.lawfulsiteparser.parser.parser import Parser
from src.lawfulsiteparser.service.parser_service import ParserService

async def main():
    print("Запуск парсера МосГорСуда...")
    print("Все данные будут сохранены в папку data/")
    print("Документы — в data/downloads/номер_дела/\n")

    async with Parser() as parser:
        service = ParserService(parser)
        await service.start_parser()

    print("\nПарсинг завершён!")
    print("Результаты: data/results.csv")
    print("Документы: data/downloads/")

if __name__ == "__main__":
    asyncio.run(main())