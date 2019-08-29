<hr>
<h2> Raj_Recipe_Cook_Book_Web_App </h2>
<hr>
Raj Recipe Cook Book Web_App is a responsive multi-pages scoal cooking blog app where user can store and read the cooking recipies.

<h2> Overview </h2>

A web application created in Python and Flask.

<h2> UX </h2>

This website was created with the intention to store and share recipes with other users. 

<h2> Features <h2> 
<p>
 
<h3> It is a fully functional user based social website that provides registered user:-  </h3>

<ul>

<li> Create new recipies - recipe name, category, servings, preparation time, cooking method etc, </li>
<li> Read all the recipies </li>
<li> Edit own recipies </li>
<li> Delete own recipies </li>
<li> Vistor can only read the recipies </li>
<li> To post a recipe visitor must sign up </li>
<li> User can see all his or her recipies on one place after login under UserName: Nav-link </li>
<li> User can update Profile picture and other info after login under Profile: Nav-link </li>

</ul>

</p>

<h3> A demo of this site is available:- <a href="https://raj-recipe-world.herokuapp.com/" rel="nofollow">here</a> </h3> 

<hr>

<div>
<h2> Getting started / Deployment </h2>

<p>

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

<h4> A demo of this site is available:- <a href="https://raj-recipe-world.herokuapp.com/" rel="nofollow">here</a> </h4>

</ul>

</p>

</div>

<hr>
<h2>Technologies Used </h2>

<h3> Built With </h3>

Python Flask-Python microframework Sqlite SQL database
AWS - S3 to store imaegs
HTML5, CSS3 and JavaScript
Bootstrap CSS framework to style and create responsive design
other Front end languages that give the application structure, style and interactivity


<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python-Version 3.7.3</a>
<ul>
<li>The project uses <strong>Python</strong> for backend development.</li>
</ul>
</li>

<li><a href="https://pypi.org/project/Flask/" rel="nofollow">Flask-Version 1.1.0</a>
<ul>
<li>The project uses <strong>Flask</strong> for backend development.</li>
</ul>
</li>


<li><a href="https://www.sqlite.org/download.html" rel="nofollow">SQLite</a>
<ul>
<li>The project uses <strong>SQLite</strong> SQL database to store the data from user</li>
</ul>
</li>


<li><a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/" rel="nofollow">Bootstrap v4.1.3</a>
<ul>
<li>The project uses <strong>Bootstrap</strong> to speed up the development.</li>
</ul>
</li>

<li><a href="https://fontawesome.com/" rel="nofollow">Font Awesome v5.3.1</a>
<ul>
<li>The project uses <strong>Font Awesome</strong> for icons.</li>
</ul>
</li>
 
<li><a href="https://code.jquery.com/jquery-3.3.1.min.js" rel="nofollow">JQuery v3.3.1</a>
 
 <ul>
<li>The project uses <strong>JQuery</strong> for better user experiences as well as to speed up the development.</li>
</ul>
</li>

<li><a href="https://cdnjs.cloudflare.com/ajax/libs/ekko-lightbox/5.3.0/ekko-lightbox.min.js" rel="nofollow">ekko-lightbox/5.3.0</a>
 
<ul>
<li>The project uses <strong>ekko-lightboxy</strong> in the gallery section to overlay images on the current page.</li>
</ul>

</li>

<li><a href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.js" rel="nofollow">slick-carousel/1.9.0/</a>
 
<ul>
<li>The project uses <strong>Slick.js</strong> for carouse.</li>
</ul>

</li>

<li><a href="https://getbootstrap.com/docs/4.3/components/forms/#validation" rel="nofollow"> HTML5, Bootstra4 and Javascripts /</a>
 
<ul>
<li>The project uses <strong> HTML5, Bootstra4 and Javascripts</strong> for form Validation.</li>
</ul>

</li>

<li> <a href="https://signin.aws.amazon.com/" rel="nofollow"> AWS /</a>

<ul>
<li>The project uses <strong> AWS - S3 </strong> to store the imaegs.</li>
</ul>



<hr>




<h2> UX Design </h2>
Details of the UX design undertaken as part of this project is available in the Wireframes subfolder of projectdocumentation folder. 
This document outlines how I approached the design of this website.

<h2> Testing </h2>

All the CRUD actions were tested and are working as it should. When updating a recipe the same is duplicated, this will be fixed later. I've added a delete button on the card so it can be deleted easily instead of the need to go to the recipe page to do so. The responsiveness was tested on every page. Every link was tested and works properly. All forms handle empty input fields


<h2> Author </h2>
<p>
Rajaneesh Singh Bhadauria - This project was completed as part of Code Institute’s Mentored Online Full Stack Web Development course in 2019.
</p>

<h2> Content </h2> 

<ul>

<li> The text for the Carousel, Menu and About sections were taken from: <a href="" rel="nofollow"> Raj </a> </li>

</ul>

<h2> Media </h2> 

<ul>

<li> The images used in this site were obtained from: <a href="https://pixabay.com/" rel="nofollow"> pixabay.com/ </a> </li>

</ul>

<h2> Content </h2> 

<ul>

<li>

The content for recipes was taken from the <a href="https://food.ndtv.com" rel="nofollow"> NDTV recipes website</a>

</li>

</ul>

<h2> Acknowledgements </h2> 

<ul>

<li> I don't cook much at home inspired me to make a tool to remeber the recipies </li>

</ul>









