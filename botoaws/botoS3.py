import numpy as np
import boto3
import os, sys
import datetime
from config import Boto3Session


#Bucket Naming Convention
#  FirstNameMiddleNameLastNameDate

currentTime = datetime.datetime.now()
currentTime = "{}{}{}".format(currentTime.month, currentTime.day, currentTime.year)

session = Boto3Session().session()

client = session.client('s3')


#create bucket
# response = client.create_bucket(
#     ACL='private',
#     Bucket='rashidhamiddar{}'.format(currentTime),
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     },
# )


#upload file to bucket
# with open('configfile.cfg', 'r') as file:
#     data = file.read()

# response = client.put_object(
#     ACL='private',
#     Body=data,
#     Bucket='rashidhamiddar{}'.format(currentTime),
#     Key='test1.txt'
# )


# delete a bucket object
# response = client.delete_object(
#     Bucket = 'rashidhamiddar{}'.format(currentTime),
#     Key = 'test.txt',
# )


# retrieve an object
# response = client.list_objects(
#     Bucket= 'rashidhamiddar{}'.format(currentTime),
# )

# list of buckets
response = client.list_buckets()
for bucket in response.get("Buckets", None):
    print(bucket.get("Name", None))
print(response)