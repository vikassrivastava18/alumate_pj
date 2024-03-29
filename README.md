Alumate
===
Overview
---
Alumate is a social platform which helps people who is preparing for study abroad, current students, and alumni.

Landing page img
---
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/landingpage1.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/landingpage2.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/landingpage3.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/landingpage4.png" alt="landing" title="sample">  

Content page img
---
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/page1.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/page2.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/page3.png" alt="landing" title="sample">  
<img src="https://raw.githubusercontent.com/ShintaG3/alumate_pj/master/Screenshot/page4.png" alt="landing" title="sample">  

Functionalities
---

Alumate shall have followinig fanctionalities.
- **Sign in**: User can sign-in from social apps. After signup, user fill their profile information, then connect existing users.  
**considering plugin**: oath2, allauth
- **User account**: User can sign-up and create own account. Profile includes: country, school, course, start-year, end-year, student status(preparing, current, alumni), previous education(school), previous job, post job, livinig location.  
**model**: AUTH_USER
- **User search**: User can search other users by: country, school, start/end year, job, living location, and follow them.
- **Feed**: User can post and see following users' posts in their feed page. In a post, user can like and comment.
- **Feed search**: There is a search box for feed
- **Notification**: When user receive like and comment on their posts, notification badge apears on the navigation bar.
- **Inquiry**: User can make a inquiry to target  users by tagging profile information. e.g. Harvard University, 2020. These inquiries appear on the feed page of the target users, regardless of following. Also, there is a inquiry page where all inquiry can be seen and searched.
- **Private Message**: User can send private message to other users.

Additional features (Pending until above features are done)
---
- **Mentor**: User can be a mentor who can intensively support other users for certain duration.
- **Restriction**: Free subscription user can send messages to only same status or less users. They cannot request mentor suport.
- **Premium**: Premium user can send message all users and can request mentor suport.

Deployment
---
Heroku

Mediafile storage
---
AWS

Folder Structure
---

```
project
├─project_name
│      settings.py
│      local_settings.py #configulation for heroku
│
├─templates           #contain templates which used accross the project
│  └─base            #contain templates used wiht xtends syntax {% extends 'base.html' %}
│       css.html
│       js.html
│       navbar.html
│    base.html
│
├─app_name            #app's folder
│  └─templates       #contain templats which used in each app
│     └─app_name     #create an app's name folder here
│        ├─base      #contain templates used with extends syntax {% extends 'base.html' %}
│        └─includes  #contain templates used with includes syntax {% includes 'format.html' %}
│
├─static
│  ├─css
│  ├─js
│  │  ├─core
│  │  └─plugins
│  └─json
│
├─media_root          #for the img files which changes regularly
│  ├─university_img
│  └─profile_img
│
├─staticfiles
│
│
├─env                 #environment file: it's heavy and should not be pushed to remoterepositry
│
│
│  .gitignore          #files which will not be pushed to remote repository
│  requirements.txt    #files which will not be pushed to remote repository
```
## Create a following local_setting.py file in "alumate" folder
```
├─alumate
│      settings.py
│      local_settings.py
```

local_settings.py
```
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}

DEBUG = True
```

## Development Environment Setup
Prerequisites: Install following first
- Python
- pip
- virtualenv
- PostgresSQL
---

### Create and activate virtual environment
```
$ virtualenv venv
$ . venv/bin/activate (Linux/Mac OS)
$ venv\Scripts\activate (Windows)
```

### Install dependencies
```
$ pip install -r requirements.txt
```

### Collect static files
You need to comment out `STATICFILES_STORAGE` in `almate/settings.py` before collecting static files. Otherwise, it refers to the production storage.
```
$ python manage.py collectstatic
```

### Migrate model
Migrate the model to sqlite file 
```
$ python manage.py migrate
```


### Run server
Make sure `DEBUG` mode is true in `almate/settings.py` before running development server.
```
$ python manage.py runserver
```
