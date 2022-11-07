import boto3
from botocore.exceptions import ClientError

sns = boto3.resource('sns')

def create_topic(name):
    try:
        topic = sns.create_topic(Name=name)
    except ClientError:
        raise
    else:
        return topic

if __name__ == '__main__':
    create_topic('sonja-sns-sdk')

