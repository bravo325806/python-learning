

### Create django project

```bash
$ django-admin.py startproject mydjango .
```

`django-admin.py`是一個可以創專案的腳本

接下來會看到資料目錄：

```
mydjango
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

`manage.py`用來管理django網站的腳本
`settings.py`包含網站中的各種設定

### Run web server 

```
python3 manage.py runserver
```

到`http://127.0.0.1:8000/`就可以看到建好的web server了！

如果8000port已經使用了，可以後面加上你要的`port`：
```
python3 manage.py runserver 3000
```
就可以看到：
Starting development server at http://127.0.0.1:3000/

### Start app

我們start一個叫`blog`的app

```
django-admin startapp blog
```

### Setting

在`settings.py`檔案中`Application definition`新增剛剛start的app`blog`

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

在`models.py`
```python
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique = True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    # Sub class Meta
    class Meta:
        ordering =['-created'] # sort this based on the date 
        def __unicolde__(self): # order for the posts to work
            return u'%s' %self.title #u'-> unicode
    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])

```
儲存後
```
python3 ./manage.py migrate
```

### Create super user

```
python3 ./manage.py createsuperuser
```
Run Server
```
python3 ./manage.py runserver 
```
到 `http://127.0.0.1:8000/admin/` 登入後就可以看到Django administration頁面了。

### Admin 

到`admin.py`

```python
from django.contrib import admin
from .models import Post # @models.py
# post model
admin.site.register(Post)
```

migrate
```
python3 ./manage.py migrate
```
看到：
```
 No migrations to apply.
 Your models have changes that are not yet reflected in a migration, and so won't be applied.
 Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
```

```
python3 ./manage.py makemigrations
python3 ./manage.py migrate
```
接著Run server
```
python3 ./manage.py runserver 
```

可以看到在admin畫面中多了`Post` 
點進去Post可以看到我們剛剛創建的`title`,`slug`,`summary`,`content`等欄位了！

### Creat Views

`urls.py`

```python
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
urlpatterns = [
    # define two routers (post,index)
    url(r'^post/$',blog_views.post),
    url(r'^$',blog_views.index),
    url(r'^admin/', admin.site.urls),
]
```

`views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hey there.")
def post(request):
    return HttpResponse("I am a single post page")
```

接著Run server
```
python3 ./manage.py runserver 
```
到 `http://127.0.0.1:8000/` 與 `http://127.0.0.1:8000/post` 就可以看到頁面了！

### Templates

在blog底下建立一個`templates`資料夾，並建立一個HTML `index.html`

```html
<!DOCTYPE html>
<body>
    <h3>hello world ! plusone!</h3>
</body>
</html>
```
更改 `views.py`的`index` function
```python
def index(request):
    return render(request,'index.html',{})
```

在網頁上就可以看到:
`
hello world ! plusone!
`


