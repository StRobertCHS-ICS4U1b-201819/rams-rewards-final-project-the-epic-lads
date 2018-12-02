<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
<img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg"></a>
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://discord.gg/NCytcfU"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg" alt="Chat"></a>
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a><br>
------


# Development

## Requirement
+ [install docker](https://docs.docker.com/install/#supported-platforms)
+ [install docker compose](https://docs.docker.com/compose/install/)
+ run `docker run hello-world` if no errors, go to next steps.

## build
Clone this repo and enter it :

    $ git clone https://github.com/StRobertCHS-ICS4U1b-201819/rams-rewards-final-project-the-epic-lads.git
    $ cd rams-rewards-final-project-the-epic-lads

Then run it on docer compose :

    $ docker-compose up --build

+ If you get a `Permission denied` error using either of the above methods, you probably do not have the proper permissions to run docker. To force the process, prepend `sudo` to either of the above commands and run again, or [change the user group](https://docs.docker.com/install/linux/linux-postinstall/)

+ If you get a `Cannot start containers: port is already allocated` error via runing `docker-compose up --build`, it most likey is some service still runing at same port, try to run `systemctl restart docker`

+ If there is any other errors, feel free to submit it on [github issues](https://github.com/StRobertCHS-ICS4U1b-201819/rams-rewards-final-project-the-epic-lads/issues)



## Edit 
To run sub-folder, we require different grammer :

    $ docker-compose run [file] [command]

### For example:

backend:

    $ docker-compose run backend python manage.py createsuperuser

frontend:

    $ docker-compose run frontend npm run lint




------

# Product Catalog

## Ram Rewards Student App (RRSA) User Stories
This mobile app will be used by students.  Students will be able to:
* View amount of rewards points earned
* View their basic info such as Name, homeroom, student id
* Swipe to reveal their student ID barcode (with barcode underneath)
* View a history of rewards activity (individual events where rewards points are earned)

## Ram Rewards Teacher Admin App (RRTAA) User Stories
This mobile app will be used by teacher and administrators to distribute rewards points to students. Teachers/Administrators will be able to:  
* Choose from a list of rewards activities (activities will have predetermined point values) to rewards points for (i.e Coding Club meeting, attend a basketball game, attend a dance.
* Reward points to a student by using the camera to scan a barcode from the student id card or the barcode from the RRSA
* Generate a rewards code to allow a teacher/facilitator to distribute points to multiple students.
* Choose a student to view their rewards activity history
* Choose a rewards activity to view student activity by date.  (i.e Coding Club activity for Nov 12th).
* Sends and recieves necessary data from/to the RR Web Administraton Console

## RR Web Administration Console User Stories
Website for Rams Rewards administrators.  RR Admins will be able to:
* Define the list of rewards activities along with their point values.
* Manage list of student accounts (add accounts, remove accounts, edit info)
* View history of rewards activity.
* View charts of rewards activity (by date, by activity)

