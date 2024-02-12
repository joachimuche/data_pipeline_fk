import pandas as pd
from faker import Faker
import awswrangler as wr
from utils import aws_session
from datetime import datetime


def profile_data_generator(df_range: int):
    sample = Faker()
    dataframe = pd.DataFrame([sample.profile() for profile in range(df_range)])

    return dataframe


def data_extract_to_s3():
    wr.s3.to_parquet(
                    df=profile_data_generator(200),
                    path=f"s3://raw-data-regional/regional_user_profile/",
                    boto3_session=aws_session(),
                    mode="append",
                    dataset=True,
                    database='testfaker',
                    table='userprofile'
                    )
    return "Data successfully written to s3"

# def extract_to_csv():
#     data = profile_data_generator(200)
#     data.to_csv(path_or_buf=f"user_profile{(datetime.now())}.csv", index=False)

# data_extract_to_s3()
data_extract_to_s3()