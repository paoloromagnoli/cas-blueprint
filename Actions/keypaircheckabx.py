import boto3
import json

def handler(context, inputs):
    ec2 = boto3.client('ec2')
    tags = inputs["tags"]
    key_name = tags["Deploy"]
    keypair = ec2.create_key_pair(KeyName=key_name)

    print(keypair)

    outputs={}
    outputs["KeyFingerprint"]=keypair["KeyFingerprint"]
    outputs["KeyMaterial"]=keypair["KeyMaterial"]
    outputs["KeyName"]=keypair["KeyName"]

    return outputs
