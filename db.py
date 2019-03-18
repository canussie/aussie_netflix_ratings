#!/usr/bin/python
"""Database operations"""
import mysql.connector
from mysql.connector.constants import ClientFlag

HOSTNAME = "localhost"
USER = "dba"
PASSWD = "XXXX"
DATABASE = "movies"
TITLES_CSV = "/tmp/titles.csv"
RATINGS_CSV = "/tmp/ratings.tsv"


def create_tables():
    """Create DATABASE tables"""
    try:
        dbconnect = mysql.connector.connect(user=USER, password=PASSWD, \
        host=HOSTNAME, database=DATABASE)
        mycursor = dbconnect.cursor()
        # create titles table
        mycursor.execute("CREATE TABLE IF NOT EXISTS titles \
        (tconst VARCHAR(255), titleType VARCHAR(255),\
        primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult VARCHAR(255),\
        startYear VARCHAR(255), endYear VARCHAR(255), runtimeMinutes VARCHAR(255),\
        genres VARCHAR(255))")
        # create ratings table
        mycursor.execute("CREATE TABLE IF NOT EXISTS ratings (tconst VARCHAR(255),\
        averageRating FLOAT, numVotes VARCHAR(255))")
    except mysql.connector.Error as fail:
        print(fail)

def import_data():
    """Import data from IMDB dumps into table"""
    try:
        dbconnect = mysql.connector.connect(user=USER, password=PASSWD, \
        host=HOSTNAME, database=DATABASE,\
        client_flags=[ClientFlag.LOCAL_FILES])
        mycursor = dbconnect.cursor()
        load_titles = "LOAD DATA LOCAL INFILE '" + TITLES_CSV + "' INTO TABLE titles"
        load_ratings = "LOAD DATA LOCAL INFILE '" + RATINGS_CSV + "' INTO TABLE ratings"
        mycursor.execute(load_titles)
        mycursor.execute(load_ratings)
        mycursor.execute("alter table titles add index (tconst)")
        mycursor.execute("alter table ratings add index (tconst)")
        dbconnect.commit()
    except mysql.connector.Error as fail:
        print(fail)

def flush_tables():
    """Flush tables from DB"""
    try:
        dbconnect = mysql.connector.connect(user=USER, password=PASSWD, \
        host=HOSTNAME, database=DATABASE)
        mycursor = dbconnect.cursor()
        tables = ["titles", "ratings"]
        for table in tables:
            mycursor.execute("DROP TABLE " + table)
        dbconnect.commit()
    except mysql.connector.Error as fail:
        print(fail)

def find_match(title, year):
    """Find matching title"""
    try:
        dbconnect = mysql.connector.connect(user=USER, password=PASSWD, \
        host=HOSTNAME, database=DATABASE)
        mycursor = dbconnect.cursor()
        query = "SELECT * FROM titles WHERE primaryTitle = \"" + title + "\" and titleType = 'tvSeries'"
        query2 = "UPDATE titles set netflix = \'1\' WHERE primaryTitle = \"" + title + "\" and titleType = 'tvSeries'"
        print query2
#        mycursor.execute(query)
        mycursor.execute(query2)
        dbconnect.commit()
#        results = mycursor.fetchall()
#        return results
    except mysql.connector.Error as fail:
        print(fail)
   

#flush_tables()
#create_tables()
#import_data()
