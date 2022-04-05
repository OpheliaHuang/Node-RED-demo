


class Data(object):
    '''collection of urls for news'''


    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, source, url):
        self.properties[source] = url
    
    def get_properties(self):
        return self.properties


class News(Data):
     def __init__(self):
        self.properties = {'bbc': 'http://feeds.bbci.co.uk/news/uk/rss.xml',
            'sky': 'http://feeds.skynews.com/feeds/rss/uk.xml'}

class Tech(Data):
     def __init__(self):
        self.properties  = {'bbc': 'http://feeds.bbci.co.uk/news/technology/rss.xml',
            'sky': 'http://feeds.skynews.com/feeds/rss/technology.xml'}



if __name__ == "__main__":
    result = News()
    #result.set_properties("bla", "test")
    print(result.get_properties()["sky"])
