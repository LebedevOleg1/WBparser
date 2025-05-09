# WbParser 🤖

Telegram-бот для анализа позиций товаров в поисковой выдаче Wildberries. Помогает отслеживать видимость товаров по ключевым запросам.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Requests](https://img.shields.io/badge/Requests-2.32.3-important)](https://docs.python-requests.org)

## 🌟 Особенности

- Автоматическая генерация ключевых слов из названия товара
- Поиск товара по 1-10 страницам выдачи Wildberries
- Определение точной позиции в поисковых результатах
- Удобный интерфейс через Telegram-бота

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/WbParser.git
cd WbParser
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте бота:
- Создайте бота через @BotFather
- Замените токен в bot.py:
```python
bot = telebot.TeleBot("ВАШ_ТОКЕН_ЗДЕСЬ")
```

## 🚀 Использование

1. Запустите бота:
```bash
python bot.py
```
2. Перейдите в Telegram и найдите вашего бота

3. Отправьте боту:
[Ссылка на товар WB]
[Количество страниц для проверки (1-10)]

Пример:
https://www.wildberries.ru/catalog/175533691/detail.aspx
3

## 📊 Пример вывода

Запрос: "мужские кроссовки": Товар найден на странице 2. Позиция 7.
Запрос: "спортивная обувь 2024": Товар не найден.
...

