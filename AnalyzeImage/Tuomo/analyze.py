import boto3
import sys
import json

if __name__ == "__main__":
    sourceFile=sys.argv[1]
    client=boto3.client('rekognition')
    print(sourceFile)

       
    imageSource=open(sourceFile,'rb')
    

    # Implement label detection using detect_lalbes method 
    # (see https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels)
    # Note: This time let's use local image i.e. you can read the contents of the image using imagesource.read()
    # Target to return if there is a match and if yes, what is the confidence %

    response = client.detect_labels(Image={'Bytes': imageSource.read()}, MinConfidence=70)

    
    #print(json.dumps(response, indent=2))

    #x = (response['Labels'])

    #print(json.dumps(x, indent=2))

    #y = (x['Name'])
    #print('-----------------------------------------------------------')
    #print(json.dumps(y, indent=2))

    x = response.keys()

    for label in response['Labels']:
        #print(label)
        #print('---------------------------')
        name = label['Name']
        #print(name)
        #print('---------------------------')
        confidence = str(label['Confidence'])
        print('Found label, name ' + name + ' confidence ' + str(confidence) + '%')
        #print('++++++++++++++++++++++++++')
    imageSource.close()
        

