import json
import boto3

def hello(event, context):
    print(json.dumps(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)

    key = event['Records'][0]['s3']['object']['key']
    print(key)

    client=boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':key}},
        MaxLabels=20, MinConfidence=60)

    labels = ""

    print('Detected labels for ' + key) 
    print()   
    for label in response['Labels']:
        labels = label['Name'] + "," + labels
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("----------")
        print ()

    s3 = boto3.client("s3")
    s3.copy_object(Key=key, Bucket=bucket,
                CopySource={"Bucket": bucket, "Key": key},
                Metadata={"labels": labels},
                MetadataDirective="REPLACE")
