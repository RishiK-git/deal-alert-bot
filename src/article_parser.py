import datetime

def format_article(article: dict) -> str:
    return (
        f"Headline: {article['headline']}\n"
        f"Date-Time: {datetime.datetime.fromtimestamp(article['datetime'])}\n"
        f"Summary: {article['summary']}\n"
        f"URL: {article['url']}\n"
        f"Source: {article['source']}\n"
        + "-" * 60
    )

def print_articles(articles: list):
    for article in articles:
        print(format_article(article))
