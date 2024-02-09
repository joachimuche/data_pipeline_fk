import pandas as pd
from faker import Faker
import awswrangler as wr
from utils import aws_sesion


def profile_data_generator(df_range: int):
    sample = Faker()

    dataframe = pd.DataFrame([sample.profile() for profile in range(df_range)])

    return dataframe


def data_extract_to_s3():

    wr.s3.to_parquet(
                    df=profile_data_generator(200),
                    path="s3://raw-data-regional/user_profile/",
                    boto3_session=aws_sesion(),
                    mode="append",
                    dataset=True
                    )
    return "Data successfully written to s3"