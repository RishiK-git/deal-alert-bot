import finnhub
from src import config 

def get_news():
    finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)
    articles = finnhub_client.general_news('general', min_id=0)
    return articles
