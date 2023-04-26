import boto3


class S3Object:
    def __int__(self):
        pass

    @classmethod
    def upload_file_to_s3(cls,
                          file,
                          bucket: str,
                          key: str,
                          server_side_encryption: str = 'AES256',
                          content_type: str = 'string',
                          acl: str = 'bucket-owner-full-control',
                          tagging: str = 'string',
                          aws_region: str = "sa-east-1",
                          aws_profile: str = None):
        aws_session = boto3.Session(profile_name=aws_profile)
        s3_resource = aws_session.resource(
            service_name='s3',
            region_name=aws_region
        )
        s3_resource.Bucket(bucket).put_object(
            Key=key,
            Body=file,
            ContentType=content_type,
            ACL=acl,
            ServerSideEncryption=server_side_encryption,
            Tagging=tagging
        )