def remove_duplicates(df):
    """Function that remove the duplicated rows and keep
    the first appearance in a pandas data frame"""

    dup_rows = df.duplicated().sum()

    if dup_rows > 0:
        df_cleaned = df.drop_duplicates(keep="first")
        print(f"{dup_rows} duplicate rows have been removed")
        return df_cleaned
    else:
        print("There are no duplicated rows in the data frame")
