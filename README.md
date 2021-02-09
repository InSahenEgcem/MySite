# MiSyte 



## Start Server

```
cd mysite
py manage.py runserver
```

To view the site click [here](http://127.0.0.1:8000/).

## How to 'Commit' in Git
How to save code into your Git Repository(Repo)

```
git add .
git commit -m "A Useful message to know what i did"
git push
```

## How to make a Directory(MKDIR)
```
MKDIR 'MiSyte'
```

## How to list out Files in Current Directory(Folder)
```
DIR
```

## How to change into a Child Directory
```
cd 'MiSyte'
```

## How to jump to Parent Directory
```
cd ..
```

## How to Add a New app to a Django Project
```
py manage.py startapp polls
```

## How to Add a 'Views' Path to my Polls app

Make a 'views' Path within The Polls app 
This Code creates a Views Path in The Polls app when put into the urls.py File

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```