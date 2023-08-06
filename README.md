# Манга сайт

## Старт проекта

Создать .env файл с .env.example ключами из директории config и заполнить их необходимыми значениями.

Установить зависимости:
pip install -r requirements.txt

Активировать виртуальное окружения:
source venv/bin/activate

Накатить миграции:
python manage.py migrate

Создать суперпользователя для доступа к админке:
python manage.py createsuperuser

Запуск тестов:
python manage.py test

Запуск приложения:
python manage.py runserver

## Панель администратора
http://localhost:8000/admin/


## Сваггер
http://localhost:8000/swagger/
