from datetime import datetime
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

class Database:

    def __init__(self):

        load_dotenv('.env') 

        self.url = "http://localhost:8086"
        self.token = os.getenv('TOKEN')
        self.org = os.getenv('ORG')
        self.bucket = os.getenv('BUCKET')
        self.id = 1

        self.client = InfluxDBClient(url="http://localhost:8086", token=self.token, org=self.org)

    def writeToDB(self, value):

        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        query_api = self.client.query_api()

        p = Point('measurement1').tag('user', 'user1').field('glucose_levels'+str(self.id), value)
        self.id = self.id+1
        write_api.write(bucket=self.bucket, record=p, org='icsd')

