# SPA Project
## Overview
This web application is to serve user for admin and customer which no not required to login. customer able to view car and its details across the landing page. as for admin, admin able to manage their cars in the admin portal. 

## Development Stack
NodeJS
React JS
Installation:
https://nodejs.org/en/
https://reactjs.org/docs/create-a-new-react-app.html

Python
Django Rest Framework
Python Web Site
https://code.visualstudio.com/docs/python/tutorial-django

WSL
https://learn.microsoft.com/en-us/windows/wsl/install

Docker
https://docs.docker.com/desktop/install/windows-install/

## Start the project
### Running Full Stack with Docker on local host
docker-compose -f docker-compose-local.yaml

cd to frontend directory
npm install
npm start

make another new terminal
cd backend
python -m venv env (CREATE a new environment)
source env/Script/activate (go into the environment)
pip install -r requirements.txt (install required packages)
python manage.py makemigrations (sync with db)
python manage.py migrate (update changes)
python manage.py runserver (RUN server)