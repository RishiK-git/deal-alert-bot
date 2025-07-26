def is_business_deal(article):
    # For now, just a dummy filter, you can improve later
    keywords = ['merger', 'acquisition', 'investment', 'partnership']
    headline = article.get('headline', '').lower()
    return any(keyword in headline for keyword in keywords)
