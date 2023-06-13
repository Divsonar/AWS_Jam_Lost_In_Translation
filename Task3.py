for index, row in df.iterrows():
    review_body = row['review_body']
    language = row['language']
    truncated_review_body = review_body[:2048]
    language_code = language
    response = comprehend_client.detect_sentiment(Text=truncated_review_body, LanguageCode=language_code)
    sentiment = response['Sentiment']
    df.at[index, 'sentiment'] = sentiment
print(df.head())
sentiment_column = df['sentiment']
sentiment_counts = sentiment_column.value_counts()
print(sentiment_counts)
