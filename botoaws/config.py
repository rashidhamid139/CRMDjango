import configparser
import boto3

# config = configparser.RawConfigParser()
# config.read('configfile.cfg')

# session = boto3.Session(
#     aws_access_key_id=config.get('IAM' ,'accesskey'),
#     aws_secret_access_key= config.get('IAM', 'secretkey'),
#     region_name='us-east-2'
# )

class Boto3Session:

    def session(self):
        config = configparser.RawConfigParser()
        config.read('configfile.cfg')

        session = boto3.Session(
            aws_access_key_id=config.get('IAM' ,'accesskey'),
            aws_secret_access_key= config.get('IAM', 'secretkey'),
            region_name='us-east-2'
        )
        return session