import os

class Config:

    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=b4cd697d9d1644d394ba25d5a93875ab'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=b4cd697d9d1644d394ba25d5a93875ab'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}