import boto3

def generate_key_url(bucket_location, bucket_name, key_name):
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        bucket_name,
        key_name
    )

s3 = boto3.resource('s3')
bucket_name = 'kristina-should-be-dataset-master'
bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)

files = s3.Bucket(bucket_name).objects.all()
urls_list = [ generate_key_url(bucket_location, bucket_name, file.key) for file in files ]

print("Bucket item count: {0}".format(len(list(files))))

with open("item_list.yml", "w+") as list_yaml:
    yaml_string = ''
    for url in urls_list:
        yaml_string += "- {{url: '{0}'}}\n".format(url)
    list_yaml.write(yaml_string)
