# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from download import download
from sklearn.linear_model import LinearRegression

# %%
# Albert 1er Totem
root_url = "https://data.montpellier3m.fr/sites/default/files/ressources"
in_file = "MMM_EcoCompt_XTH19101158_archive.json"
# Preprocessing:
download(os.path.join(root_url, in_file),
         os.path.join("./", in_file), replace=False)
out_file = in_file.split(".")[0]+"_new"+".json"
if not os.path.isfile(out_file):
    # 1) remove white lines
    with open(in_file, "r") as f, open(out_file, "w") as outfile:
        for i in f.readlines():
            # 2) create new lines when errors }{ occurs
            # (due to network issues according to MMM)
            i = i.replace("}{", "}\n{")
            if not i.strip():
                continue
            if i:
                outfile.write(i)
# %%
# Reading the file in a dataframe
print(in_file)
dfct = pd.read_json(out_file, lines=True,
                    dtype={"intensity": float})
print("read done")
dfct[["day_start", "day_stop"]] = dfct.dateObserved.str.split("/", expand=True)
dfct.head()
# %%
# Clean time indexing.
date_to_keep = "day_start"
dfct_new = dfct[[date_to_keep, "intensity"]]
dfct_new[date_to_keep] = pd.to_datetime(dfct_new[date_to_keep])
dfct_new = dfct_new.sort_index(ascending=True)

# %%
# Shift in report from MMM: the report the day before!!!
dfct_new = dfct_new.shift(periods=1)
dfct_new = dfct_new.set_index(['day_start'])
dfct_new.dropna(inplace=True)
# Remark: Monday=0,..., Sunday=6.
dfct_new['weekday'] = (dfct_new.index.weekday)
dfct_new['weekday']
days = ['Lundi', 'Mardi', 'Mercredi',
        'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

plt.bar(days, dfct_new.groupby(['weekday'])["intensity"].mean())
days_week = dfct_new.groupby(['weekday'])["intensity"].mean()

# %%
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(dfct_new['intensity'], '.-')
all_fridays = dfct_new['intensity'][dfct_new["weekday"] == 4]
n_fridays = len(all_fridays)

OLS = LinearRegression()
OLS.fit(np.array(np.arange(n_fridays-1)).reshape(-1, 1),
        all_fridays[:-1].values)
friday_predict_ols = OLS.predict(np.array([n_fridays]).reshape(-1, 1))[0]
print(friday_predict_ols)
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(all_fridays, '.-')

# %%
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
download(url, os.path.join("./", "Totem.csv"), replace=False)
# %%
df_totem = pd.read_csv("./Totem.csv", skiprows=[0, 1])
df_totem.head(10)
df_totem.columns = ['day', "time", "year_tot_counts", "day_counts", "a", "b"]
df_totem.drop(columns=["year_tot_counts", "a", "b"], inplace=True)
# %%
df_totem["DateTime"] = pd.to_datetime(
    df_totem['day'] + ' ' + df_totem['time'], format="%d/%m/%Y %H:%M:%S")
df_totem["day"] = pd.to_datetime(df_totem['day'], format="%d/%m/%Y")
df_totem = df_totem.set_index(['DateTime'])
df_totem.dropna(inplace=True)
df_totem.sort_index(ascending=True, inplace=True)

# %%
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(df_totem['day_counts'], '.-')
df_totem.head(10)
# %%
# Fill new values with NaN, then add total day.
# XXX TODO: use a merge function for this loop.
NaN = np.nan
df_totem["total_day"] = NaN
for time in df_totem.index:
    try:
        df_totem.at[time, "total_day"] = dfct_new.at[str(time.date()),
                                                     "intensity"]
    except KeyError:
        print("nope")

# %%
df_totem.dropna(inplace=True)
df_totem.tail(20)
df_totem["prop"] = df_totem['day_counts'] / df_totem["total_day"]
df_totem.head(20)
# %%
df_totem['weekday'] = df_totem.index.day_name()  # Monday=0, Sunday=6
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
# %%
# Predictions
rush_hour = df_totem.between_time('08:40', '09:20')
rush_hour.groupby(['weekday'])['prop'].median()

# Prediction based on last Wednesday + intraday density:
print("Perdict the coming Friday from the last Wednesday:")
friday_predict_wednesday = days_week[4.0] / days_week[2.0]
median_rush_hours = rush_hour.groupby(['weekday'])['prop'].median()
print(friday_predict_wednesday * median_rush_hours['Friday']
      * dfct_new.at['2021-03-31', "intensity"])
print("Ratio of bikes before 9AM per day of week:")
print(median_rush_hours)

# Prediction based on OLS over Fridays + intraday density:
print("OLS on Fridays:")
print(friday_predict_ols * median_rush_hours['Friday'])
# %%
