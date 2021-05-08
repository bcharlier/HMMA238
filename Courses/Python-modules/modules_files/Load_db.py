import pandas as pd
from download import download
from biketrauma.io import url_db, path_target


class Load_db:
  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=False)

  def print_df(self):
    print(self.save_as_str()) #print(Load_db.save_as_str(self))

  def save_as_str(self):
    return str(Load_db.save_as_df()) #print(self.save_as_str())
  
  @staticmethod
  def save_as_df():
    df_bikes = pd.read_csv(path_target, na_values="", low_memory=False, converters={'data': str, 'heure': str})
    return df_bikes
