import boto3
import os

def upload_file(path, bucket):
    with open(path, 'rb') as data:
        file_name = os.path.basename(path)
        bucket.put_object(Key = file_name, Body = data)

s3 = boto3.resource('s3')
bucket_name = 'kristina-should-be-dataset-master'
bucket = s3.Bucket(bucket_name)
directory = './img'

for file in os.listdir(directory):
    upload_file(os.path.join(directory, file), bucket)
