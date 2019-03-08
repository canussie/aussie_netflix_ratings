#!/usr/bin/python

import scrape
import db

SHOWS = scrape.getshowlist()

#print SHOWS

try:
    for title, year in SHOWS.iteritems():
        #print title
        #print year
        #print type(year)
        result = db.find_match(title, year)
        print result
except KeyboardInterrupt:
    print "Quitting"
