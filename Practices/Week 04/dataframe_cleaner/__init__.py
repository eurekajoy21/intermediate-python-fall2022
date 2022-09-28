import pandas as pd

def drop_empty(df):
  return df.dropna()

def fill_empty(df, col_name):
  df[col_name] = df[col_name].fillna(df[col_name].mean())
  return df

def drop_column(df, col_name):
  return df.drop(col_name, axis=1)

def fix_index(df):
  return df.reset_index(drop=True)

def fix_dates(df, col_name):
  df[col_name] = pd.to_datetime(df[col_name])
  return df
