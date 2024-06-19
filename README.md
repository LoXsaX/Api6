# Публикуем комикс в телеграм
## Описание
Этот проект сделан для того, чтобы автоматизировать сбор комиксов и их публикации в Telegram
## Описание
Скачайте необходиые файлы, затем используйте `pip`(или `pip3`, если есть конфликты с Python2) для установки зависимостей. Зависимости можно установить командой, представленной ниже. Создайте бота у отца ботов. Создайте новый канал Telegram.

Установите зависимости командой:

```
pip install -r requirements.txt
```
## Пример запуска из скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для публикации комиксов необходимо написать:
```
python upload_telegram.py
```
## Переменные окружения 
Часть настроек проекта берется из переменных окружения. Переменные окружения - это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл `.env` и запишите туда данные в таком формате: Переменная = значение.
Пример содержания `.env`:

`TG_TOKEN = 'tg_token'`

`CHAT_ID = 'chat_id'` 

Получить токен `TG_TOKEN` можно у отца ботов.