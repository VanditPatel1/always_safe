import boto3
import time

""" Store this file in .gitignore or in enviroment outside git repo """
from AWS_CREDS import DEFAULT_BUCKET, ACCESS_KEY_ID, SECRET_ACCESS_KEY


class S3_Conn:
    """ Class to easily interact with S3 """

    def __init__(self, bucket=None):
        self.region = None
        self.bucket = bucket or DEFAULT_BUCKET
        self.aws_id = ACCESS_KEY_ID
        self.aws_secret = SECRET_ACCESS_KEY
        self._cli = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
        self.s3 = self._cli.meta.client


    def upload_file(self, local_path, s3_path):
        print ("Starting file upload...")

        try:
            start = time.time()
            self.s3.upload_file(local_path, self.bucket, s3_path)
            end = time.time()
            print ("Upload took {0} seconds".format(end-start))

        except Exception as ex:
            print (ex)
            raise

    def ls_all(self, bucket=None):
        b = bucket or self.bucket
        list_obj = self.s3.list_objects_v2(Bucket=b)
        response = list_obj['Contents']
        return response

    def ls_key(self, prefix, bucket=None):
        b = bucket or self.bucket
        prefix = str(prefix) #boto3 expects a string

        try:
            list_obs = self.s3.list_objects_v2(Bucket=b, Prefix=prefix)
        except Exception as ex:
            print ("Error finding files with prefix: {0} in bucket: {1}".format(prefix, bucket))
            raise
