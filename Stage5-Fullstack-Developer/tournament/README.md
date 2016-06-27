
Project: Tournament Planner
===========================
Udacity IPND Nanodegree: Stage 5 - Back End Path ( Final Project )

In this project, I’ll be writing a Python module that uses the PostgreSQL
database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each
round: players are not eliminated, and each player should be paired with another
player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema
(SQL table definitions), and writing the code that will use it.

A more detailed guide can be found in the link below
https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true


How to run
----------
Before you begin ensure you have the following installed:
	•	VirtualBox
	•	Vagrant
	•	Git


Using Git
---------
	1.	Fork the repository (Click Fork in the top-right corner)
	2.	Clone the newly forked repository to your computer.
	3.	Then from the terminal, cd to your desired directory and run:

        $ git clone PASTE_PATH_TO_REPO_HERE tournament

This will give you a directory named tournament


Start the virtual machine
-------------------------
Using the terminal, change directory to tournament/vagrant
(cd tournament/vagrant), then launch your virtual machine using:

      $ vagrant up

This will also run the config.sh script which will create the tournament
database.


SSH into the machine
-------------------
      $ vagrant ssh


Move to the correct directory
-----------------------------
      $ cd /vagrant/tournament


Run tests
---------
      $ python tournament_test.py
