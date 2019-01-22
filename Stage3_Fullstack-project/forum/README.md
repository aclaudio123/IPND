
Project: Web Forum server
===========================
Udacity IPND Nanodegree: Stage 5 - Back End Path ( Fullstack Project)


How to run
----------
Before you begin ensure you have the following installed:
	1.	VirtualBox
	2.	Vagrant
	3.	Git


Using Git
---------
	1.	Fork the repository (Click Fork in the top-right corner)
	2.	Clone the newly forked repository to your computer.
	3.	Then from the terminal, cd to your desired directory and run:

		       $ git clone PASTE_PATH_TO_REPO_HERE forum

This will give you a directory named forum


Start the virtual machine
-------------------------
Using the terminal, change directory to forum/vagrant
(cd forum/vagrant), then launch your virtual machine using:

      $ vagrant up

This will also run the pg_config.sh script which will create the forum
database.


SSH into the machine
-------------------
      $ vagrant ssh


Move to the correct directory
-----------------------------
      $ cd /vagrant/forum


Run tests
---------
      $ python forum.py
      http://localhost:8000
