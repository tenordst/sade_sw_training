import boto3
import sys
import json

if __name__ == "__main__":
    sourceFile=sys.argv[1]
    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')

    # Implement label detection using detect_lalbes method 
    # (see https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels)
    # Note: This time let's use local image i.e. you can read the contents of the image using imagesource.read()
    # Target to return if there is a match and if yes, what is the confidence %

    imageSource.close()
