import json
import boto3 # used to get the textract service in our Python code


def display_text(response, extract_by):
    # 
    line_text = []
    for block in response["Blocks"]:
        if block["BlockType"] == extract_by:
            line_text.append(block["Text"]) # 
    return line_text


def lambda_handler(event, context):
    textract = boto3.client("textract")
    if event: # the event==True when S3 recieves a document
        file_obj = event["Records"][0] # get the current event
        bucketname = str(file_obj["s3"]["bucket"]["name"]) #get bucket name from event
        filename = str(file_obj["s3"]["object"]["key"]) #get file name from event



        response = textract.detect_document_text( 
        # a call to textract API to just extract text (detect_document_text), then we state the bucket name and file name
            Document={
                "S3Object": {
                    "Bucket": bucketname,
                    "Name": filename,
                }
            }
        )
        print(json.dumps(response)) # print the extracted data

        
        raw_text = display_text(response, extract_by="LINE") # pass response to display_text() so
        print(raw_text)
