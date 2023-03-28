### Description
This is full stack code of POC. 
As of now, it uses django as framework and django-ninja is being used to develop the required apis.
Apis are integrated with the help of AJAX and django-templating.


### Configuring FastApi
1. Enable venv
2. `pip install -r req.txt`
3. Because currently this application uses sqlite as database so no need to run db migration command and sample data is also present in data base.
4. For database migrations and table creation/updation in database if using some other databse like postgres/mysql:
  - `python manage.py makemigrations`
  - `python manage.py migrate`


### Running development web server after activating virtual env
1. `python manage.py runserver`
2. Api doc swagger url: `http://localhost:8000/api/docs`
3. Url to access default admin panel: `http://localhost:8000/admin` 
4. URl to access custom admin panel:  http://localhost:8000/ 

### Super admin 
- username: adi
- password: 12345678

### Normal user creds
- username: shivam
- password: 8423845784Me#


- All credentials can be used to login in both panel: default admin panel and custom panel.