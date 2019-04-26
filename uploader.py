import boto3
import os

def upload_file(path, bucket):
    data = open(path, 'rb')
    file_name = os.path.basename(path)
    bucket.put_object(Key = file_name, Body = data)

s3 = boto3.resource('s3')
bucket = s3.Bucket('kristina-should-be-dataset-master')
directory = './img'

for file in os.listdir(directory):
    upload_file(os.path.join(directory, file), bucket)