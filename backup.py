from s3_connector import S3_Conn
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

s = S3_Conn()

s.upload_file("abc.txt", "l/test.txt")
a = s.ls_all()
b = s.ls_key(prefix='')


pp.pprint(a)

print ("-------")

pp.pprint(b)


def save_dir()
