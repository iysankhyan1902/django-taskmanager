# Django Task Manager

A simple task management web application built with Django, featuring user authentication, priority-based task filtering, and AWS S3 integration for media storage.

## Features

- User registration, login, logout

- Edit profile + upload profile picture (stored in AWS S3)

- Create, update, delete tasks

- Filter tasks by priority (High, Medium, Low)

- Pagination for task list

- Clean UI using Bootstrap and Crispy Forms

- Media storage using AWS S3 + django-storages

## Tech Stack

Backend: Python, Django 5
Frontend: HTML, CSS, Bootstrap 4, Crispy Forms
Cloud Storage: AWS S3 (django-storages + boto3)
Database: SQLite (development)
Utilities: python-dotenv, Pillow

## Installation
1. Clone the Repository
git clone https://github.com/iysankhyan1902/django-taskmanager.git
cd django-taskmanager

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Add Environment Variables

### Create a .env file in the root:

SECRET_KEY=your_django_secret_key

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=ap-south-1


.env is already ignored by .gitignore.

## Run the Project
python manage.py migrate
python manage.py runserver


### Visit:

http://127.0.0.1:8000/

## Project Structure
todo_project/
│
├── task/             
├── users/            
├── templates/        
├── static/           
├── .env              
├── manage.py

## AWS S3 Integration

Uses django-storages + boto3

Files uploaded via Django models/forms go directly to S3

Public object access via CLEAN URLs (no signed querystrings)

Bucket policy enables read-only public access
