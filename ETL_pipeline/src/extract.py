import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning
    so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):
    """ """

    rs_connection = connect_to_redshift(dbname, host, port, user, password)

    query = """select ot.invoice,
                      ot.stock_code,
                      ot.quantity,
                      cast(ot.invoice_date as datetime) as invoice_date,
                      ot.price,
                      ot.customer_id,
                      ot.country,
                      -- coalesce(sd.description, 'Unknown') as description
                      case when sd.description is null
                      then 'UNKNOWN'
                      else sd.description end as description
               from bootcamp.online_transactions ot
               left join (select *
                          from bootcamp.stock_description
                          where description <> '?') sd on
                          ot.stock_code = sd.stock_code
               where ot.customer_id <> '' and
               ot.stock_code not in ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
            """

    # Reading the data from redshift
    online_trans_cleaned = pd.read_sql(query, rs_connection)

    print(
        "The shape of the extracted and transformed"
        " data is", online_trans_cleaned.shape
    )

    return online_trans_cleaned
