import  pandas as pd

def get_accident(df_bikes, log_scale=True):
  gd = df_bikes.groupby(['departement']).size()
  if log_scale:
    gd = np.log(gd)
  return gd
