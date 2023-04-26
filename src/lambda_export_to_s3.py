from datasources.s3 import S3Object
import json
import requests as re

REGION = "sa-east-1"
BUCKET = "general-bucket-test"
PATH = "ci_cd_raw/"


def lambda_handler(event, context):
    #pokemon = event.get("pokemon")
    pokemon = "lucario"
    print(f"Pokemon: {pokemon}")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = re.get(url)
    response_json = response.json()
    response_bytes = json.dumps(obj=response_json,
                                ensure_ascii=False,
                                separators=(',', ':')).encode('utf8')

    key = PATH + pokemon + ".json"

    S3Object.upload_file_to_s3(file=response_bytes,
                               bucket=BUCKET,
                               key=key,
                               content_type='application/json',
                               aws_region=REGION,
                               aws_profile=None)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }