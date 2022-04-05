import os
import pandas as pd
from flask import (Flask, 
Response,
jsonify,
request, 
url_for,
make_response)
import config
from models import scraper, news

#######################################################################################



app = Flask(__name__)
app.config['SECRET_KEY'] = config.Config.SECRET_KEY
count = 435
available = ["news", "tech"]

########################################################################################

########################################################################################

''' For making requests, the pattern is:

/all : for full dictionary with current news across all sources
/category/<type> : gives news across one category currently "news" or "tech" from all available sources
/category/<type>/<source> : gives the selected type of news from your selected source

'''



@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'



@app.route('/all', methods=['GET'])
def return_all_data():
    urls = []
    for category in available:
        data = eval("news." + category.capitalize() + "()")
        cat_urls = data.get_properties().values()
        urls += cat_urls
    result = scraper.Scrape()
    print(urls)
    result.urls = urls
    response = result.news_rss()
    return jsonify(response)




@app.route('/category/<category>/<channel>', methods=['GET'])
def return_channel_data(channel=None, category = None):
    
    if category not in available:
        response = "Valid types are: news, tech. "   
        return jsonify(response)
    else:
        data = eval("news." + category.capitalize() + "()")

        urls = data.get_properties()[str(channel)]
        result = scraper.Scrape()
        result.urls = [urls]
        response = result.news_rss()
        return jsonify(response)


@app.route('/category/<category>', methods=['GET'])
def return_category_data(channel=None, category = None):
    if category not in available:
        response = "Valid types are: news, tech. "   
        return jsonify(response)
    else:
        
        data = eval("news." + category.capitalize() + "()")
        urls = data.get_properties().values()
        result = scraper.Scrape()
        result.urls = urls
        response = result.news_rss()
        return jsonify(response)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0',port=port)
