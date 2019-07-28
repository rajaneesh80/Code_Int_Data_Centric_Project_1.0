Recipe_app Web App

Demo: 

Overview

A web application created in Python and Flask.

UX

This website was created with the intention to store and share recipes with other users. 

Features
Create new recipes - recipe name, category, level of difficulty, servings, preparation time, method, ingredients.
Read recipes
Edit recipes
Delete recipes

Technologies Used

Bootstrap
CSS framework to style and create responsive design
Python
Flask
Python microframework
Sqlite
SQL database

Testing
All the CRUD actions were tested and are working as it should. When updating a recipe the same is duplicated, this will be fixed later. I've added a delete button on the card so it can be deleted easily instead of the need to go to the recipe page to do so. The responsiveness was tested on every page. Every link was tested and works properly. All forms handle empty input fields.

Deployment

This project was deployed at Heroku
Create requirements.txt

pip3 freeze --local requirements.txt

Create Procfile

echo web: python app.py > Procfile

Create Heroku App

Set Config Vars adding IP and PORT on Heroku app settings

 IP 0.0.0.0
 PORT 5000
Login to Heroku on the terminal

 Heroku login
Deploy to Heroku

 Scale the app's web process to 1 dyno: heroku ps:scale web=1
 git remote add https://git.heroku.com/cookbook-app-flask.git
 git push heroku master