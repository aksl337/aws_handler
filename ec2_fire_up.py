#!/bin/python
import boto3

ec2 = boto3.resource('ec2')
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
