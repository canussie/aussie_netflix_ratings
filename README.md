# aussie_netflix_ratings
Project to link Aussie Netflix TV Series with Ratings such as IMDB

This is work in progress, I hope to build a complete web app to display the information and allow users to view the data in multiple ways.

## PreReqs

  - Get the imdb titles and ratings datadumps https://datasets.imdbws.com/.
  - Install mariadb server, python mysql libraries, start the services
  - Setup a user, create a database named movies, grant the user all rights to the database

## Quick start

1. Configure db.py, create_tables() and import_data().
2. Run compare.py

You will now have a database containing 2 tables, titles and ratings. A query can be run to find all the netflix (field netflix = 1) TV shows, a join can be made to the ratings table to match up the titles with ratings.

## Future

I hope to expand this into a web app that will dynamically display information from the database, this is a work in progress.

## db.py

Used to clean tables, create tables and import IMDB data into movies database.

Configure the variables in db.py to reflect on your enviroment. Point the titles and ratings variables at uncompressed copies of the downloaded imdb datadump files.

Run db,py to create the create_tables() and import_data() functions to create the titles and ratings tables, then import from the downloaded dumps.

## scrape.py

Module to scrape data from finder.com.au. 

## compare.py

Run this script once db.py has been configured and data has been imported. This script does the following:

  - Runs scrape.py, which returns an array containing TV show names and year produced.
  - Loops through array and checks if it exists in the titles database.
  - If a match is found the field netflix is set to 1 (True).





