#!/usr/bin/env python
import boto3
import clipboard


ec2 = boto3.resource('ec2')


def list_ec2():
    for instance in ec2.instances.all():
        instance.load()
        print(instance.id, instance.state, instance.public_dns_name)
        if instance.state['Name'] == 'running' or instance.state['Name'] == 'pending':
            clipboard.copy(instance.public_dns_name)


list_ec2()
