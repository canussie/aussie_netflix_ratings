#!/usr/bin/python

import mysql.connector
from mysql.connector.constants import ClientFlag

hostname="localhost"
user="dba"
passwd="password1234"
database="movies"
titles_csv="/tmp/titles.csv"
ratings_csv="/tmp/ratings.tsv"


def create_tables():
    try:     
        db=mysql.connector.connect(user=user, password=passwd, host=hostname, database=database)
        mycursor=db.cursor()
        # create titles table
        mycursor.execute("CREATE TABLE IF NOT EXISTS titles (tconst VARCHAR(255), titleType VARCHAR(255), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(255), startYear VARCHAR(255), endYear VARCHAR(255), runtimeMinutes VARCHAR(255), genres VARCHAR(255))") 
        # create ratings table
        mycursor.execute("CREATE TABLE IF NOT EXISTS ratings (tconst VARCHAR(255), averageRating FLOAT, numVotes VARCHAR(255))")
    except Exception as F:
        print F

def import_data():
    try:
        db=mysql.connector.connect(user=user, password=passwd, host=hostname, database=database, client_flags=[ClientFlag.LOCAL_FILES])
        mycursor=db.cursor()
        load_titles = "LOAD DATA LOCAL INFILE '" + titles_csv + "' INTO TABLE titles"
        load_ratings = "LOAD DATA LOCAL INFILE '" + ratings_csv + "' INTO TABLE ratings"
        mycursor.execute(load_titles)
        mycursor.execute(load_ratings)
        db.commit()
    except Exception as F:
        print F

create_tables()
import_data()

