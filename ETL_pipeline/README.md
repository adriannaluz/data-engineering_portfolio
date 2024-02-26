## ETL-Pipeline
The main goal of this project is to combine all of my known tools to create an ETL (Extract, 
Transform, Load) pipeline. This will be use as the foundation of many of my data related projects:
- [Customer Segmentation](https://github.com/adriannaluz/data-analysis_portfolio/tree/customer_segmentation/customer_segmentation)

### Description
In this project I extracted 400k transactions from Redshift using PostgreSQL. Applied a first 
cleaning filter by excluding faulty entries using Python. Transformed the data by removing all
the duplicated rows. Finally, the cleaned data was load into Amazon S3.

### Requirements 
To be able to use my ETL pipeline project you will need
- Python 3
- Python libraries: 
  - psycopg2 (to establish the connection with Redshift)
  - pandas (to access and manipulate the data)
  - boto3 (to establish the connection to AWS S3 bucket) 
  - dotenv (to load the .env file)
  - datetime (to print the execution time)

### How to use this project?
First of all, clone the repo:
```
git clone --depth 1 --branch etl-pipeline --single-branch git@github.com:adriannaluz/data-engineering_portfolio.git
```
You will get a folder called ETL_pipeline with the following structure:

```
├── ETL_pipeline
│   ├── env.example
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   └── src
│       ├── extract.py
│       ├── load_data_to_s3.py
│       └── transform.py
```

The scripts located in the src folder will help you to perform single tasks like:
- [Extract the data](https://github.com/adriannaluz/data-engineering_portfolio/blob/etl-pipeline/ETL_pipeline/src/extract.py)
- [Transform the data](https://github.com/adriannaluz/data-engineering_portfolio/blob/etl-pipeline/ETL_pipeline/src/transform.py)
- [Load the data to a AWS S3 buket](https://github.com/adriannaluz/data-engineering_portfolio/blob/etl-pipeline/ETL_pipeline/src/load_data_to_s3.py)

With the script [main.py](https://github.com/adriannaluz/data-engineering_portfolio/blob/etl-pipeline/ETL_pipeline/main.py) you will perform all the ETL tasks at once and print the execution time.

> [!IMPORTANT]
> To establish the connection with the servers, you will need and .env file with the credentials
> of Redshift and AWS. An example in provided in the repo wit the name [env.example](https://github.com/adriannaluz/data-engineering_portfolio/blob/etl-pipeline/ETL_pipeline/env.example).






