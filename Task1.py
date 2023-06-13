s3_client = boto3.client('s3')
source_bucket = '<>' # Insert S3 Bucket Name Here
source_key = 'comprehend-language-sentiment/reviews_books_mixed_languages.csv'
destination_file_path = 'reviews_books_mixed_languages.csv'
s3_client.download_file(source_bucket, source_key, destination_file_path)
print('File copied successfully!')
csv_file_path = 'reviews_books_mixed_languages.csv'
df = pd.read_csv(csv_file_path)
