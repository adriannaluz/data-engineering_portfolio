import os
import warnings

from c import datetime
from dotenv import load_dotenv
from src.extract import extract_transactional_data
from src.transform import remove_duplicates
from src.load_data_to_s3 import df_to_s3

# removing warning messages
warnings.filterwarnings("ignore")

# loading variables from .env file
load_dotenv()

# Redshift connection credentials
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")

# aws-s3 connection credentials
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key_id")

start_time = datetime.now()

# Conecting to redshift and extracting the data
print("Extracting data from redshift")
online_trans = extract_transactional_data(dbname, host, port, user, password)
ot_rows, ot_col = online_trans.shape
print(
    f"There are {ot_rows} rows and {ot_col} columns on the online transaction"
    f" table"
)

# Removing duplicates
print("Removing duplicated rows")
online_trans_cleaned = remove_duplicates(online_trans)
otc_rows, otc_col = online_trans_cleaned.shape
print(
    f"There are {otc_rows} rows and {otc_col} columns on the cleaned"
    f" online transaction table"
)

# Defining the key and the name of the s3 bucket where the data will be safe
key = "transformations_final/ag_online_trans_transformed.pkl"
s3_bucket = "sep-bootcamp"

# Loading the data to a s3 bucket
print("Loading data in aws")
df_to_s3(online_trans_cleaned,
         key,
         s3_bucket,
         aws_access_key_id,
         aws_secret_access_key
         )

execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")
