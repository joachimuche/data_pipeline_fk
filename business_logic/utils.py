import boto3


def aws_sesion():
    session = boto3.Session(
        # aws_access_key_id=Variable.get("access_key"),
        # aws_secret_access_key=Variable.get("secret_access_key"),
        
        aws_access_key_id='lxbXJSDhFboeJSxGh3pfW2YOBYfBZIj/VMkWTIQ2',
        aws_secret_access_key='AKIASWZHRVTXOJDM5KZW',
        region_name="eu-central-1"
    )
    return session
