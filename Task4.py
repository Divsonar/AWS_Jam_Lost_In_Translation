filtered_df = df[df['sentiment'] == 'NEGATIVE']
filtered_df = filtered_df.reset_index(drop=True)
print(filtered_df)
new_df = filtered_df['review_id']
print(new_df)
new_df.to_csv('analysis_results.csv', index=False)

csv_file_path = 'analysis_results.csv'
bucket_name = '<>' # Insert S3 Bucket Name Here
s3_key = 'analysis_results.csv'
s3_client = boto3.client('s3')
s3_client.upload_file(csv_file_path, bucket_name, s3_key)
print('File saved to S3 successfully!')
