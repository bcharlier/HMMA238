import os
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from download import download
# %%
root_url = "https://data.montpellier3m.fr/sites/default/files/ressources"

files = [
    "MMM_EcoCompt_X2H19070220_archive.json",
    "MMM_EcoCompt_X2H20042632_archive.json",
    "MMM_EcoCompt_X2H20042633_archive.json",
    "MMM_EcoCompt_X2H20042634_archive.json",
    "MMM_EcoCompt_X2H20042635_archive.json",
    "MMM_EcoCompt_X2H20063161_archive.json",
    "MMM_EcoCompt_X2H20063162_archive.json",
    "MMM_EcoCompt_X2H20063163_archive.json",
    "MMM_EcoCompt_X2H20063164_archive.json",
    "MMM_EcoCompt_XTH19101158_archive.json"
    ]

# old_files = [
# "MMM_EcoCompt_X2H19070220_Archive2020.json",
# "MMM_EcoCompt_X2H20042632_Archive2020.json",
# "MMM_EcoCompt_X2H20042633_Archive2020.json",
# "MMM_EcoCompt_X2H20042634_Archive2020.json",
# "MMM_EcoCompt_X2H20042635_Archive2020.json",
# "MMM_EcoCompt_X2H20063161_Archive2020.json",
# "MMM_EcoCompt_X2H20063162_Archive2020.json",
# "MMM_EcoCompt_X2H20063163_Archive2020.json",
# "MMM_EcoCompt_X2H20063164_Archive2020.json",
# "MMM_EcoCompt_X2H20063164_archive.json",
# "MMM_EcoCompt_XTH19101158_Archive2020.json",
# ]

# Preprocessing:
for in_file in files:
    download(os.path.join(root_url, in_file),
             os.path.join("./", in_file), replace=False)
    out_file = in_file.split(".")[0]+"_new"+".json"
    if not os.path.isfile(out_file):
        # 1) remove white lines

        with open(in_file, "r") as f, open(out_file, "w") as outfile:
            for i in f.readlines():
                # 2) create new lines when }{ occurs.
                i = i.replace("}{", "}\n{")
                if not i.strip():
                    continue
                if i:
                    outfile.write(i)

    # %%
    print(in_file)
    dfct = pd.read_json(out_file, lines=True,
                        dtype={"intensity": float})
    # %%
    print("read done")
    dfct.head()

    dfct[["day_start", "day_stop"]] = dfct.dateObserved.str.split("/", expand=True)

    # %%
    date_to_keep = "day_start"
    dfct_new = dfct[[date_to_keep, "intensity"]]
    dfct_new[date_to_keep] = pd.to_datetime(dfct_new[date_to_keep])
    dfct_new = dfct_new.set_index(['day_start'])
    dfct_new = dfct_new.sort_index(ascending=True)

    days = ['Lundi', 'Mardi', 'Mercredi',
            'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    dfct_new['weekday'] = dfct_new.index.weekday  # Monday=0, Sunday=6

    # %%
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(dfct_new['intensity'],'.-')

    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees  
    plt.tight_layout()
    # %%
    plt.figure()
    plt.bar(days, dfct_new.groupby(['weekday'])["intensity"].mean())

# %%
