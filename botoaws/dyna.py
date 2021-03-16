import os
import sys
import datetime
import time
from config import Boto3Session

# session = Boto3Session().session()
# db = session.resource('dynamodb')
# table = db.Table("Sensor")
# response = table.get_item(
#     Key={
#         'Sensor_id': "1",
#     }
# )


class MyDB:
    def __init__(self, table_name="Sensor", ):
        self.table_name = table_name
        self.session = Boto3Session().session()
        self.db = self.session.resource('dynamodb')
        self.table = self.db.Table(table_name)
        self.client = self.session.client('dynamodb')

    

    def get(self, Sensor_id='1'):
        response = self.table.get_item(
            Key={
                "Sensor_id": Sensor_id,
            }
        )
        return response["Item"]

    def set(self, Sensor_id='', Temprature='', Humidity=''):
        self.table.put_item(
            Item={
                'Sensor_id': Sensor_id,
                "Temprature": Temprature,
                'Humidity': Humidity,
            }
        )

    def delete(self, Sensor_id=''):
        self.table.delete_item(
            Key={
                'Sensor_id': Sensor_id,
            }
        )

    def describe_table(self):
        response = self.client.describe_table(
            TableName = 'Sensor'
        )
        return response



obj = MyDB(table_name='Sensor')
print(obj.get(Sensor_id='2'))