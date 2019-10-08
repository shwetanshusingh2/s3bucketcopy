import boto3
import botocore
from botocore.client import ClientError
import zipfile,os


os.environ['AWS_SHARED_CREDENTIALS_FILE'] = "C:/Users/Hp/.aws/credentials"

os.environ['AWS_PROFILE'] = "default"
os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"


import urllib.request
data = urllib.request.urlopen("https://raw.githubusercontent.com/shwetanshusingh2/s3bucketcopy/master/lambdafunction.py")
f = open("filename.py",'w')

for line in data:
    f.write(line.decode('utf-8'))

f.close()

s3 = boto3.resource('s3')
lab_session = boto3.Session()
c = lab_session.client('s3')
client = boto3.client('cloudformation')
#source = os.environ['source_bucket']
#dest = os.environ['dest_bucket']

def upload_zip_file():
    try:
        s3 = boto3.resource('s3')
        s3.create_bucket(Bucket='data-shwet', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
    except ClientError:
        print("cool")
    s3.Object('data-shwet', 's3creation.yaml').upload_file(Filename='C:\\Users\\Hp\\PycharmProjects\\untitled4\\ss.yaml')
    #s3.Object("data-shwet", "ss.yaml").upload_file(Filename="ss.yaml")
    #locfile = "https://raw.githubusercontent.com//shwetanshusingh2//s3bucketcopy//master//lambdafunction.py"
    zip = zipfile.ZipFile ("myfile.zip", "w")
    zip.write ("filename.py")
    zip.close()
    s3.Object('data-shwet', 'myfile.zip').upload_file(Filename='myfile.zip')
    s3 = boto3.resource('s3')

#checks for the stack creation
def create_new_stack():
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

        except Exception as e:
            print(e)

        response = client.delete_stack(StackName='str5')


        #waits till the stack is deleted before it creates the new stack

        stack = client.describe_stacks(StackName='str5')
        while stack['Stacks'][0]['StackStatus'] =='DELETE_IN_PROGRESS' :
            try:
                stack = client.describe_stacks(StackName='str5')
            except Exception:
                 break

        response=client.create_stack( StackName='str5', TemplateURL=r"https://data-shwet.s3.ap-south-1.amazonaws.com/s3creation.yaml" ,Capabilities=['CAPABILITY_NAMED_IAM'])
        #print("ending exception\n")


upload_zip_file()
create_new_stack()
