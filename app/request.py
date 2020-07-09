from app import app
import urllib.request,json
from .models import source
from .models import article

Article = article.Article

Source = source.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting source url

source_url = app.config["NEWS_SOURCE_URL"]

#Getting topic url
topic_url =

def get_news_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)

    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            print(source_results_list)
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process the JSON object and converts them to a list of objects
    
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def news_article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results


def get_news_by_topic(topic_name):
    '''
    function that gets the response to the category json
    '''
    get_topic_url = topic_url.format(topic_name,api_key)
    print(get_topic_url)
    with urllib.request.urlopen(get_topic_url) as url:
        get_topic_data = url.read()
        get_topic_response = json.loads(get_topic_data)

        get_topicy_results = None

        if get_topic_response['articles']:
            get_topic_list = get_topic_response['articles']
            get_topic_results = process_articles_results(get_topic_list)

    return get_topic_results