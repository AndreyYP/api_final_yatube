### Проект api_final_yatube позволяет с помощью запросов к API
### создавать/удалять/редактировать посты, группы и комментарии
Аутентификация выполнена с помощью JWT токена.

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
Примеры запросов можно посмотреть в redoc:
```
http://127.0.0.1:8000/redoc/
```
