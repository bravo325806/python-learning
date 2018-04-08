# Flask Web with PostreSQL Database

## System
* Flask
* PostgreSQL
* Python3

## Create First Flask web app
* 建立一個`app.py`的檔案，用來定義與執行此應用程式。在`Flask`要建立一個程式的進入點只需要匯入它`(import flask class)`，並且初始及實例化：
```python
app = Flask(__name__)
```
* 記得再加上：
```python
if __name__ = '__main__':
    app.run()
```
這段程式碼是為了自動執行flask class內所有的function。

* 當然，這樣還沒有結束，現在我們要簡單的建立一個網頁的畫面顯示`Hello World!`，請加上以下程式碼：
```python
@app.route('/')
def index():
    return 'Hello World!'
```

* 加上DEBUG模式，當程式碼更改的時候會自動重整而且可以看到更細節的錯誤訊息：(記得將config的內容都加在`app.run()`前)
```python
app.config['DEBUG'] = True
```
* 執行`app.py`後，可以看到`Running on http://127.0.0.1:5000/`這表示我們的程式碼已經執行起來了，並且在`5000`port。到[localhost:5000](http://127.0.0.1:5000/)看一下是否有畫面，就可以看到Hello World !
* 沒有的話請檢查是否是`5000`，不是的話請自行更改！

那我們第一個Flask web app就完成了！

## Initialize a Database Object
那接下來要建立資料庫了，Flask內有`Flask-Alchemy`可以用來操作`PostreSQL`。沒有的話請先用`pip`安裝起來！

* 你可以直接在`app.py`內直接新增程式碼，或是分開到另外一個`models.py`，並且加上：
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

## PostgreSQL Configure
* 在Flask內有提供語法讓我們輕易連接PostgreSQL，只需要將`postgresql://`的內容更改成自己資料庫的設定。

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
```
* 或是習慣分開設置也可以，像這個樣子:
```python
POSTGRES = {
    'user': 'plusone',
    'password': 'my_password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES
```

* 現在我們必須加上`db.init_app(app)`連接我們的應用程式，不過在這之前請先`import db`到`app.py`。
* `附註:`我將`models`分開寫所以`import models`。
```python
from models import db
# your app config  
db.init_app(app)
```

### Define Models Class

在前面Configure時我們已經定義好要的Database了，現在要來新增資料庫表格。
* 在Model Class內定義我們的表格內容：
```python
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable=False)
    birthday = db.Column(db.String(10))
    phone = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True) 
```
* `__tablename__`：定義表格名稱。
* `id`, `name`, `birthday`, `phone`, `email`為我們表格內的`column`名稱（根據自己需求去定義）。

### Create Manager 
現在建立好Class了，最後，我們要透過`flask_script`及`flask_migrate`模組來執行資料庫的`migrations`。先建立一個`manage.py`檔案。
```python
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

```
* 因為需要能夠執行`manage.py`中`migration`指令，所以最後需要加上：
```python
if __name__ == '__main__':
    manager.run()
```

### Finally, Migrations and Update!
* 在終端機執行：
```shell
$ python manage.py db init
```
* 會看到你的專案底下多了一個`migrations`的資料夾，執行manage檔案的`db migrate`產生新的`Migration`到`migrations`資料夾。
```shell
$ python manage.py db migrate
```
可以更改`alembic`設定成你想要的樣子，接著更新它：
```shell
$ python manage.py db upgrade
```

* 資料庫中的`migration`有任何更改或更新版本，都可以在`alembic_version`看到。
* 如下圖，包含了`alembic_version`table以及`users`table.

![Imgur](https://i.imgur.com/zmp3J3D.png)


