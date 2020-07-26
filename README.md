# IE-GalleryProject


## How to run

1. Install `python`(3), `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/engiAsadi/IE-GalleryProject`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/engiAsadi/IE-GalleryProject && cd IE-GalleryProject
  virtualenv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
  python manage.py createsuperuser
  ```

4. Run `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000).

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python`(3), `pip`, `virtualenv` 
2. Clone the project using:  `git clone https://github.com/engiAsadi/IE-GalleryProject`.
3. Make Environment Ready Like This:
``` Command Prompt
cd IE-GalleryProject
virutalenv -p "PATH\TO\Python.exe" build # Give Full Path To python.exe
build\Scripts\activate # Activate The Virutal Environment
pip install -r requirements.txt
python manage.py migrate # Create Database Tables
python manage.py createsuperuser
```
4. Run `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000).


## TODO
- [x] login, logout, register of backend.
- [x] crud backend.
- [x] like dislike backend.
- [x] managing template files and 
- [x] linear gradiant
- [x] like button at front (using ajax).
- [x] platograph
- [x] replacing footer
- [ ] adding scripts for back to top button




create database, user in mysql commands:
create database gallery;
create user gallery_user@localhost identified by '1234';
grant all privileges on gallery.* to gallery_user@localhost;
flush privileges;
