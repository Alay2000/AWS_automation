import boto3


def createbucket(bucket_name, bucket_location='None'):
    if bucket_location is None:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=bucket_location)
        location = {'LocationConstraint': bucket_location}
        s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    return "created"



def listallbuckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print('The Existing Buckets on the AWS account are: ')
    for buck in response['Buckets']: 
        print(f' {buck["Name"]}')
    return response



def creationTime():
    s3_resource = boto3.client('s3')
    creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
    creation_date.strftime("%d%m%y_%H:%M:%s")

    for bucket in s3_resource.list_buckets()["Buckets"]:
        print(bucket["Name"])
        print(bucket["CreationDate"])
    return 'listed in py console for now'
    


def getbucketpolicy(bucket_name):
    s3_resource = boto3.client('s3')
    return s3_resource.get_bucket_policy(Bucket=bucket_name)


def deletebucketpolicy(bucket_name):
    s3_resource = boto3.client('s3')
    return(s3_resource.delete_bucket_policy(Bucket=bucket_name))


def uploadfile(file_name, bucket_name):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket_name, object_name)
    return "uploaded"

