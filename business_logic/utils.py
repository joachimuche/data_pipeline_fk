import boto3
import boto3.session
import os
from dotenv import load_dotenv

load_dotenv()

def aws_session():
    session = boto3.session.Session(
        # aws_access_key_id=Variable.get("access_key"),
        # aws_secret_access_key=Variable.get("secret_access_key"),
        
        aws_access_key_id= os.getenv('access_id'),
        aws_secret_access_key=os.getenv('secret_id'),
        region_name="eu-central-1"
    )
    return session
