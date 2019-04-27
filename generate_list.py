import yaml
import boto3

s3 = boto3.resource('s3')
files = s3.Bucket('kristina-should-be-dataset-master').objects.all()

for file in files:
    print(file)