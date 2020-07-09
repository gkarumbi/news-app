from app import app
import urllib.request,json
from .models import Source
from .models import Article
from .models import Topic
from .models import Headline 

Article = article.Article
Source = source.Source
Headline = headline.Headline
Topic = topic.Topic

# Getting api key
api_key = None

#Getting source url

source_url = None

#Getting topic url
topic_url = None

def configure_request(app):
    global api_key,source_url,topic_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config["NEWS_SOURCE_URL"]
    topic_url = app.config["TOPIC_API_URL"]

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
            get_topic_results = process_topic_results(get_topic_list)

    return get_topic_results

def process_topic_results(topics):
    '''
    function that processes the json files of articles from the api key
    '''
    topic_source_results = []
    for topic in topics:
        author = topic.get('author')
        description = topic.get('description')
        time = topic.get('publishedAt')
        url = topic.get('urlToImage')
        image = topic.get('url')
        title = topic.get ('title')

        if url:
            topic_objects = Topic(author,description,time,url,image,title)
            topic_source_results.append(topic_objects)

    return topic_source_results

def get_trending():
    '''
    Function that get news
    '''
    get_trending_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_trending_url)
    with urllib.request.urlopen(get_trending_url) as url:
        get_trending_data = url.read()
        get_trending_response = json.loads(get_trending_data)

        get_trending_results = None

        if get_trending_response['articles']:
            get_trending_list = get_trending_response['articles']
            get_trending_results = process_articles_results(get_trending_list)

    return get_trending_results
