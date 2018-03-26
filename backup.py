from s3_connector import S3_Conn


s = S3_Conn()

s.upload_file("test.txt", "/test/test.txt")
