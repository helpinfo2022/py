import boto3

def print_info():
    client = boto3.resource('ec2')

    data = client.instances.all()

    info = {}

    for instance in data:
        print(f'instance id: {instance.id}')
        print(f'image id: {instance.image_id}')
        print(f'platform details: {instance.image.platform_details}')
        print(f'ip: {instance.network_interfaces_attribute[0]["PrivateIpAddress"]}')
        print(f'dns: {instance.network_interfaces_attribute[0]["PrivateDnsName"]}')
        print(f'subnet_id: {instance.subnet_id}')
        print(f'interface_id: {instance.network_interfaces_attribute[0]["NetworkInterfaceId"]}')
        print(f'subnet_id: {instance.state["Name"]}')
        print(f'descriiption: {instance.image.description}')
        print('tags')
        for tag in instance.tags:
            for key, value in tag.items():
                print(f'\t{key}: {value}')
        print('cpu')
        for key, value in instance.cpu_options.items():
            print(f'\t{key}: {value}')
        print(f'ram: {instance.ramdisk_id}')
        print(f'instance_type: {instance.instance_type}')
        print('security_groups')
        for group in instance.security_groups:
            for key, value in group.items():
                print(f'\t{key}: {value}')
        print(f'client_token: {instance.client_token}')
    return True


