from src.news_fetcher import get_news
from src.filter_engine import is_business_deal

def main():
    articles = get_news()

    for article in articles:
        if is_business_deal(article):
            print(f"Business Deal Found: {article['headline']}")
            print(f"URL: {article['url']}")
            print('-----------------------------------')

if __name__ == "__main__":
    main()
