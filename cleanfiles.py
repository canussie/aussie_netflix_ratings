#!/usr/bin/python

import scrape
import re

titles = "/tmp/titles.csv"

# get shows from scrape
SHOWS = scrape.getshowlist()
# load titles from file, put lines in array
fo = open(titles, "r")
titlelist_orig = fo.readlines()
fo.close()
#print SHOWS
# delete line one from titles file
del titlelist_orig[0]
# strip out movies
regex = re.compile(r'^tt\d{7}\s*(movie|tvEpisode|video|videoGame).*')
titlelist = filter(lambda i: not regex.search(i), titlelist_orig)
#print titlelist[0]
newlist = []
try:
    for show in SHOWS:
        #if any(show in s for s in titlelist):
        #    print show
        for title in titlelist:
            if show in title:
                #print show
                #print title
                print title
                newlist.append(title)
                break
        #print title
        #print year
        #print type(year)
    fo = open("new.csv", "w+")
    line = fo.writelines(newlist)
    fo.close()    
except KeyboardInterrupt:
    print "Quitting"
    fo = open("test.txt", "w+")
    line = fo.writelines(newlist)
    fo.close()
