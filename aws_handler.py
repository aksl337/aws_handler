#!/bin/python
import boto3
import clipboard
from time import sleep
import sys

ec2 = boto3.resource('ec2')


def list_ec2():
    for instance in ec2.instances.all():
        instance.load()
        print instance.id, instance.state, instance.public_dns_name
        if instance.state['Name'] == 'running' or instance.state['Name'] == 'pending':
            dns_name = instance.public_dns_name
            clipboard.copy(dns_name)


list_ec2()


def fire_up():
    instance = ec2.create_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 8,
                    'VolumeType': 'gp2',
                },
            },
        ],
        ImageId='ami-5d055232',
        KeyName='your ssh pem key',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        SecurityGroupIds=['sg-2c631344'],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'ubuntu'
                    },
                ]
            },
        ]
    )

    print instance[0].id


sleep(1)
fire_up()
sleep(15)
list_ec2()
sleep(3)
sys.exit(0)
