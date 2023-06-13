comprehend_client = boto3.client('comprehend')
for index, row in df.iterrows():
    review_body = row['review_body']
    truncated_review_body = review_body[:2048]
    response = comprehend_client.detect_dominant_language(Text=truncated_review_body)
    languages = response['Languages']
    dominant_language = languages[0]['LanguageCode']
    df.at[index, 'language'] = dominant_language
print(df.head())
language_column = df['language']
language_counts = language_column.value_counts()
print(language_counts)
