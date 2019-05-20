import os

class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?language=en&apiKey={}"
    ARTICLE_API_BASE_URL= "https://newsapi.org/v2/everything?sources={}&apiKey={}"
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config:The parernt configuration class with General configuration settings
    """
    DEBUG = True

config_options={
'development': DevConfig,
'production':ProdConfig
}
