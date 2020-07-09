from app import app

# Getting api key
api_key = app.config['MOVIE_API_KEY']

#Getting source url

source_url = app.config['NEWS_SOURCE_URL']

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
            source_results = process_results(source_results_list)

    return source_results