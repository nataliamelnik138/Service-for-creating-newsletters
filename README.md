## Сервис для создания рассылок

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

### Технологии:
- python 3.11
- django 4.2.2
- PostgreSQL

### Функции:
- авторизация и добавление пользователей с разными ролями
- настройка периодичности и автоматической отправки писем
- сбор статистики
  
### Инструкция по развертыванию проекта:

Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/Service-for-creating-newsletters
```
Запуск:
1. Создайте виртуальное окружение
```
python -m venv venv
```
2. Активируйте виртуальное окружение
```
venv/Skripts/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
6. Создайте в папке проекта файл .env, который должен содержать значение переменных из файла .env.sample
7. Примените миграции
```
python manage.py migrate
```
6. Запустите проект
```
python manage.py runserver
```

Автор проекта: Мельник Наталья
