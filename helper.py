import boto3
import botocore
from botocore.client import ClientError
import zipfile,os
id1=0;
s3 = boto3.resource('s3')
lab_session = boto3.Session()
c = lab_session.client('s3')
#source = os.environ['source_bucket']
#dest = os.environ['dest_bucket']
try:
    s3.create_bucket(Bucket='data-shwet', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
except ClientError:
    print(ClientError)
s3.Object('data-shwet', 's3creation.yaml').upload_file(Filename='C:\\Users\\Hp\\PycharmProjects\\untitled4\\ss.yaml')
locfile = "C:\\Users\\Hp\\PycharmProjects\\untitled4\\venv\\myfile.py"
loczip = "C:\\Users\\Hp\\PycharmProjects\\untitled4\\venv\\myfile.zip"
zip = zipfile.ZipFile (loczip, "w")
zip.write (locfile,os.path.basename(locfile))
zip.close()
s3.Object('data-shwet', 'myfile.zip').upload_file(Filename='C:\\Users\\Hp\\PycharmProjects\\untitled4\\venv\\myfile.zip')
client = boto3.client('cloudformation')
s3 = boto3.resource('s3')

#checks for the stack creation

try:
    #print("cool\n")
    response=client.create_stack( StackName='str5', TemplateURL=r"https://data-shwet.s3.ap-south-1.amazonaws.com/s3creation.yaml" ,Capabilities=['CAPABILITY_NAMED_IAM'])
except  client.exceptions.AlreadyExistsException:
    print("starting exception\n")
    try:
        #deletes the non emty buckets

        bucket = s3.Bucket('shwet2323')
        bucket1 = s3.Bucket('shwet32')
        bucket.objects.all().delete()
        bucket1.objects.all().delete()

    except Exception:

        print("starting second exception")
        response = client.delete_stack(StackName='str5')
        id1=1;
        print("ending second exception")


    if id1==0:
        print("abort 2nd except")
        response = client.delete_stack(StackName='str5')


    #waits till the stack is deleted before it creates the new stack

    stack = client.describe_stacks(StackName='str5')
    while stack['Stacks'][0]['StackStatus'] =='DELETE_IN_PROGRESS' :
        try:
            stack = client.describe_stacks(StackName='str5')
        except Exception:
             break

    response=client.create_stack( StackName='str5', TemplateURL=r"https://data-shwet.s3.ap-south-1.amazonaws.com/s3creation.yaml" ,Capabilities=['CAPABILITY_NAMED_IAM'])
    print("ending exception\n")



