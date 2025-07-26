import finnhub
import datetime
def main():

    finnhub_client = finnhub.Client(api_key="d21sk9pr01qquiqo258gd21sk9pr01qquiqo2590")


    # getting articles
    articles = finnhub_client.general_news('general', min_id=0)

    # parsing through articles and printing in readable format
    for article in articles:
        print("Headline: " + article['headline'])
        print("Date-Time:", datetime.datetime.fromtimestamp(article['datetime']))
        print("Summary: " + article['summary'])
        print("URL: " + article['url'])
        print("Source: " + article['source'])
        print("------------------------------------------------------------")




if __name__ == "__main__":
    main()
