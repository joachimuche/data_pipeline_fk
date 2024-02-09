import boto3


def aws_session():
    session = boto3.Session(
        # aws_access_key_id=Variable.get("access_key"),
        # aws_secret_access_key=Variable.get("secret_access_key"),
        
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name="eu-central-1"
    )
    return session
