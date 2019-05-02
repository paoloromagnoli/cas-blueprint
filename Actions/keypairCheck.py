import boto3
import json

def handler(context, inputs):
    ec2 = boto3.client('ec2')
    tags = inputs["tags"]
    key_name = tags["Deploy"] #Name of the tag used to create the key pair
    outputs = {}
    
    try:
        response = ec2.describe_key_pairs(KeyNames=[key_name,],)
    except:
        outputs["keypair_exists"] = 0
    else:
        if response is not None:
            outputs["keypair_exists"] = 1
            outputs["response"] = response

    return outputs
