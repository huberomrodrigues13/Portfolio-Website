# Portfolio-Website
## Overview
This repository contains my personal portfolio website, built using **Python**, **Flask**, **HTML**, and **CSS**.

The goal of this project was to challenge my current knowledge of flask and have a central location 
for looking at all my personal project, education, and account links all in one place. This project 
is another full-stack back-end heavy website that uses HTML and CSS for front-end visuals/styling 
and python + Flask for back-end systems designing.


## Project Structure
The project is organized into several key python files and folders:
  + webapp folder = 
    + templates folder = Collection of all the front-end templates
      + base.html = The 'main' template that all others inherit from to have the same main styling choices
      + homepage.html = Template Where the user is first welcomed with when they see my website
      + education.html = Template of my current education and past schools that I went to.
      + skills.html = Template where the user can see my current skills
      + project(n).html = Template of project 'n', where n is the project number the user will see. 
    + routes.py = where all the url routes and their endpoint functions are written, including the views and authenticated routes
    + init.py   = where the function called by main is created, making a instance of flask app with blueprints initialized from the routes file
  + main.py = where the app gets created and run locally by

## Setup
### To run this web app yourself, you will need to install the following(via pip):
  + flask
  + flask_sqlalchemy

#### To install the required Python packages, you can use the following commands:
    pip install flask
    pip install flask_sqlalchemy

    
#### Below is all the libraries from any packages installed and their versions when the project was created:
    blinker==1.9.0
    click==8.2.1
    colorama==0.4.6
    Flask==3.1.1
    Flask-SQLAlchemy==3.1.1
    greenlet==3.2.3
    Jinja2==3.1.6
    MarkupSafe==3.0.2
    typing_extensions==4.14.0

#### After everything has been installed and cloned, you can run the app using:
    python main.py
Then open your browser and go to: http://127.0.0.1:5000/


## Live Link
(In progress)

## Features
- Minimalist but eye-pleasing page format
- HTML templating with Jinja2
- Split projects with video/screenshots
- Project showcase with descriptions and links
- Responsive layout built with HTML/CSS
- Flask-based routing and template rendering
- Easy-to-update structure for adding new content
