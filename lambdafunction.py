import boto3
import os
s3 = boto3.resource('s3')
source = os.environ['source_bucket']
dest= os.environ['dest_bucket']


def myfunc(event, context):
    bucket = s3.Bucket(source)

    #bucketName = process.env.S3_BUCKET;
    dest_bucket = s3.Bucket(dest)
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.all():
        dest_key = obj.key
        print(dest_key)
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})