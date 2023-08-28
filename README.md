## Проект парсинга номеров и статусов PEP

### Описание
Асинхронный парсер для сайта python.org
Парсер выводит собранную информацию в два файла .csv:
- Список всех PEP: номер, название и текущий статус.
- Сводка по статусам PEP, количество документов в каждом из статусов и общее количество PEP документов.

### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git clone git@github.com:Rederickmind/scrapy_parser_pep.git
```
**Установите и активируйте виртуальное окружение:**
```
python -m venv venv
source venv/Scripts/activate
```
**Обновите менеджер pip и установите зависимости**
python -m pip install --upgrade pip
pip install -r requirements.txt

**Для запуска парсера введите команду в терминал:**
```
scrapy crawl pep
```
Данные сохраняются в файлах.csv в директории results/ в корне проекта

**Технологии:**
- Python 3.9.10
- Фреймворк Scrapy 2.5.1

### Автор проекта:

Никита Лёвушкин, когорта ЯП 19+
