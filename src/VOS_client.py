import boto3
from botocore.client import Config
from src.utillity import read_config_file


class VOSClient:
    def __init__(self):
        parser = read_config_file('dev.ini')
        self.access_key = parser.get('VOS', 'access_key')
        self.secret_key = parser.get('VOS', 'secret_key')
        self.s3_host = parser.get('VOS', 's3_host')
        self.bucket = parser.get('VOS', 'bucket_name')

        config = Config(signature_version='s3', s3={'addressing_style': 'path'})

        self.client = boto3.resource('s3', aws_access_key_id=self.access_key,
                                     aws_secret_access_key=self.secret_key,
                                     endpoint_url=self.s3_host, config=config)

    def download_file(self, key, bucket=None, dest='./queries/insert_dump.sql'):
        # folder/file, bucket, dest
        with open(dest, 'wb+') as file:
            if bucket:
                self.client.Bucket(bucket).download_fileobj(key, file)
            else:
                self.client.Bucket(self.bucket).download_fileobj(key, file)
