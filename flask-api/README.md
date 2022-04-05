# Simple Python Flask Dockerized Application that parses RSS feeds, sorts them and returns json#

You need Docker installed. 

just clone and run startapp.sh on linux, it will start a detached docker container called flask on Port 5000. 


For making requests, the pattern is:

# /all : for full dictionary with current news across all sources

# /category/<type> : gives news across one category currently "news" or "tech" from all available sources

# /category/<type>/<\source> : gives the selected type of news from your selected source
