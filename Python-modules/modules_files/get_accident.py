import  pandas as pd

def get_accidents(df_bikes, log_scale=True):
  gd = df_bikes.groupby(['departement']).size()
  if log_scale:
    gd = np.log(gd)
  return gd
