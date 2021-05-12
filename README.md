# Базовый шаблон
### Инициализация окружения
* Установим ```pipenv```: ```pip3 install pipenv```
* Нужно пройти в рабочую директорию
* Инициализируем окружение: ```pipenv shell``` (```exit``` - для закрытия окружения)
* Установим в окружение несколько зависимостей: 
```pipenv install flask python-dotenv```
  
## Создание базового шаблона
### Шаг 1.
* Определим точку входа в приложение ```manage.py``` или ```main.py```
* Определим проектную директорию (проектный пакет) ```app/```. 
  Добавим в директорию ```app/__init__.py```
* Определяем ядро ```app/__init__.py```
```
"""
Ядро приложения
"""
from flask import Flask

app = Flask(__name__)

```

* Научимся запускать через входную точку ```manage.py``` или ```main.py```
```
"""
Входная точка доступа в приложение
"""
from app import app

if __name__ == "__main__":
    app.run()
```
### Шаг 2.
Стандартные настройки Flask такие, как порт и отключенный debug, нам не подходят. 
Так же не задано окружение.
Задать руками можно так:
```
# manage.py
...
if __name__ == "__main__":
    app.run(port=8080, debug=True)
```
#### Как не хардкодить параметры запуска Flask приложения?
```.flaskenv``` - создадим файл с таким название в корне проекта, в нем будут содержаться 
переменные окружения, необходимые для валидной работы текущего ```Flask``` приложения.

Внутри данного файла напишем:
```
FLASK_APP = manage.py
FLASK_RUN_PORT = 8080
FLASK_DEBUG = 1
FLASK_ENV = development
```
***Важно*** - перезапустите окружение!
* После перезапуска-подъем приложения осуществляется командной ```flask run```

#### Flask CLI. Возможности.
По умолчанию Flask CLI имеет 2 команды:
* ```flask run```
* ```flask shell``` - открывает интерпретатор с загрузкой всех зависимостей приложения (но не запускает сервер).

Для того, чтобы удобно использовать ```flask shell``` нам нужно настроить контекстный процессор.

```
# manage.py
"""
Входная точка доступа в приложение
"""
from app import app

@app.shell_context_processor
def make_shell_context():
    """
    Возвращает словарь для flask shell
    где ключ - это короткое имя, через которое можно получить
    доступ к объекту (value) возвращенного словаря
    """
    return {
        "app" : app,
    }
if __name__ == "__main__":
    app.run()
```
### Шаг 3. Configs
Для хранения внутренних конфигурационных файлов приложения часто используют классический ```.env``` файл. 
Так же создадим его в ***корне*** приложения.
```
# Inner Configs
SECRET_KEY = "hj123g12ei12ue1vgid1g12d21g91od1g"
```
***Важно*** - перезапустим окружение!
* Для удобного конфигурирования приложения создадим пакет ```app/configs/__init__.py```
* В модуле ```__init__.py```
```
"""
Модуль конфигурирования базового 
конфигурационного класса приложения
"""
import os

class Config(object):
    """
    Атрибуты соответствуют полям конфигуратора
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "1234567890"
```
### Шаг 4. Присоединяем конфигурационный файл для объекта app.
* Заходим в ```app/__init__.py```:
```
"""
Ядро приложения
"""
from flask import Flask
from app.configs import Config

app = Flask(__name__)
app.config.from_object(Config)
```
### Шаг 5. Базовый шаблон готов.
Можно запускать приложение
* ```pipenv shell```
* ```flask run```