from flask import render_template
from app import app
from .request import get_news_source,news_article_source,get_news_by_topic

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'

    source_from_views= get_news_source()
    message = 'Hello World'
    return render_template('index.html', uhondo = message, title = title, sources_in_html = source_from_views)

@app.route('/source/<id>')

def news_source(id):
    '''
    View all articles from a particular news source e.g ABC News
    '''

    articles_in_view = news_article_source(id)

    return render_template('source.html',articles_in_html = articles_in_view,id=id)

@app.route('/topics/<topic_name>')
def news_by_topic(topic_name):
    '''
    View All news categorised by topic e.g health politics etcs
    '''
    topic_in_views = get_news_by_topic(topic_name)
    title  = f'{topic_name}'
    topic= topic_name

    return render_template('topics.html', title = title , topic_in_html = topic_in_views, topic = topic_name)
