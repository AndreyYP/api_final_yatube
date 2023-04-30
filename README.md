### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndreyYP/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```
Примеры запросов:

```
http://127.0.0.1:8000/api/v1/posts/ - GET запрос вернет список постов, POST запрос создаст пост
```
```
http://127.0.0.1:8000/api/v1/groups/ - GET запрос вернет список групп, POST запрос недоступен
```
```
http://127.0.0.1:8000/api/v1/jwt/create/ - POST запрос получить JWT токен, в теле запроса необходимо отправить user и password
```
