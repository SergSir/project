Версия python - 3.9

## Установка виртуального окружения
```
python -m venv venv
```
## Активация виртуального окружения

```
venv\Scripts\activate  # windows
```
## Установка зависимостей
```
python -m pip install --upgrade pip
```
Установка:
```
pip install -r .\requirements.txt
```

## Запуск сервера
```
python server/manage.py runserver
```

## Запуск Миграции
```
python manage.py migrate
```