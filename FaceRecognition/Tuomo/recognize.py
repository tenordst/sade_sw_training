import boto3
import sys

if __name__ == "__main__":
    sourceFile=sys.argv[1]
    targetFile=sys.argv[2]
    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    # Implement face recognition using compare_faces method 
    # (see https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.compare_faces)
    # Target to return if there is a match and if yes, what is the similarity %


    imageSource.close()
    imageTarget.close()