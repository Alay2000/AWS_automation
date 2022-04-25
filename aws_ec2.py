import boto3, os

def create_instance(keyname):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    key_pair = ec2_client.create_key_pair(KeyName=keyname)

    private_key = key_pair["KeyMaterial"]

    with os.fdopen(os.open("/tmp/%s.pem" %keyname, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(private_key)
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t4g.nano",
        KeyName=keyname
    )

    print(instances["Instances"][0]["InstanceId"])
    return 'created'

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
    return 'in py console'


def get_running_instances():
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
    return "printed in py console for now"


def stop_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)
    return 'Instance stopped'


def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)
    return 'Terminated'


def reboot_instance(instance_id):

    ec2 = boto3.client('ec2',region_name="us-west-2")
    ec2.reboot_instances(InstanceIds=[instance_id])
    return 'rebooted'

def describe_instance(instance_id):
    ec2 = boto3.client('ec2',region_name="us-west-2")
    response = ec2.describe_instances(InstanceIds=[instance_id])
    print(response)
    return 'in py console for now'