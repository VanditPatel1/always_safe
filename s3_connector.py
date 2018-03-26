import boto3
import time
from AWS_CREDS import *


class S3_Conn:
    """ Class to easily interact with S3 """

    def __init__(self, bucket=None):
        self.region = None
        self.bucket = bucket or DEFAULT_BUCKET
        self.aws_id = ACCESS_KEY_ID
        self.aws_secret = SECRET_ACCESS_KEY
        self.s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)


    def upload_file(self, local_path, s3_path):
        print ("Starting file upload...")
        start = time.time()

        try:
            s3.meta.client.upload_file(local_path, self.bucket, s3_path)
        except Exception as ex:
            print (ex)
        
        end = time.time()
        print ("Upload took {0} seconds".format(end-start))
