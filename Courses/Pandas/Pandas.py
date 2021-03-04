#!/usr/bin/env python
# coding: utf-8

# # First steps in  *pandas*
#
# ***
# > __Auteur__: Joseph Salmon
# > <joseph.salmon@umontpellier.fr> , adapted from the notebook by Joris Van den Bossche:
# https://github.com/jorisvandenbossche/pandas-tutorial/blob/master/01-pandas_introduction.ipynb

# <a id="intro"> </a>
#
# # Introduction et présentation

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact  # widget manipulation
from download import download
pd.options.display.max_rows = 8


# ## Case 1: Titanic dataset

# %%

url = "http://josephsalmon.eu/enseignement/datasets/titanic.csv"
path_target = "./titanic.csv"
download(url, path_target, replace=False)  # if needed `pip install download`

# df: data frame
df_titanic_raw = pd.read_csv("titanic.csv")


# %%

df_titanic_raw.tail(n=3)

# %%
df_titanic_raw.head(n=5)


# ## Missing values / manquantes:
# simplest strategy (when you can): remove all NAs

# %%

df_titanic = df_titanic_raw.dropna()
df_titanic.tail(3)


# # Description: see also https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic3info.txt

# survival: 	Survival 	0 = No, 1 = Yes
# pclass: 	Ticket class 	1 = 1st, 2 = 2nd, 3 = 3rd
# sex: 	Sex
# Age: 	Age in years
# sibsp: 	# of siblings / spouses aboard the Titanic
# parch: 	# of parents / children aboard the Titanic
# ticket: 	Ticket number
# fare: 	Passenger fare
# cabin: 	Cabin number
# embarked: Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton

# Note: an extended version of the dataset is available here:
# https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic.txt
# %%

df_titanic.describe()


# ## Visualization:

# **Age repartition**

# %%

plt.figure(figsize=(5, 5))
plt.hist(df_titanic['Age'], density=True, bins=25)
plt.xlabel('Age')
plt.ylabel('Proportion')
plt.title("Histogramme de l'âge des passagers")


# %%

plt.figure(figsize=(5, 5), num='jfpwje')
# KDE: kernel density estimate from seaborn package
ax = sns.kdeplot(df_titanic['Age'], shade=True, cut=0, bw=0.1)  #bw: bandwith
plt.xlabel('Proportion')
plt.ylabel('Age')
ax.legend().set_visible(False)
plt.title("Estimation de la densité de l'âge des passagers")
plt.tight_layout()


# ### <font color='red'> EXERCISE : density over histogram </font>
# Plot the density estimate over the histogram

# %%

plt.figure(figsize=(5, 5))
plt.hist(df_titanic['Age'], density=True, bins=50)
plt.xlabel('Age')
plt.ylabel('Proportion')
plt.title("Histogramme de l'âge des passagers")
ax = sns.kdeplot(df_titanic['Age'], shade=True, cut=0, bw=0.2,color='red')
ax.legend().set_visible(False)
plt.tight_layout()


# ## Widget
# Interactive interaction with codes and output is nowdays easier and easier
# (see also Shiny app in R-software).
# In python one can use for that `widgets` and the `interact` package.
# We are going to visualize that on the simple KDE and histograms examples.

# %%

def hist_explore(n_bins=24, alpha=0.25, density=False):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.hist(df_titanic['Age'], density=density,
            bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel('Age')
    plt.ylabel('Density level')
    plt.title("Histogram for passengers' age")
    plt.tight_layout()
    plt.show()


# %%

interact(hist_explore, n_bins=(1, 50, 1), alpha=(0, 1, 0.1), density=False)


# %%

def kde_explore(bw=5):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    sns.kdeplot(df_titanic['Age'], bw=bw, shade=True, cut=0, ax=ax)
    plt.xlabel('Age (in year)')
    plt.ylabel('Density level')
    plt.title("Age of the passengers")
    plt.tight_layout()
    plt.show()


# %%

interact(kde_explore, bw=(0.001, 2, 0.01))


# ## `Groupby` function
# How is the survival rate change w.r.t. to sex?

# %%

df_titanic_raw.groupby('Sex')[['Survived']].aggregate(lambda x: x.mean())


# How is the survival rate change w.r.t. the class?

# %%

df_titanic.columns


# %%

plt.figure()
df_titanic.groupby('Pclass')['Survived'].aggregate(lambda x: x.mean()).plot(kind='bar')
plt.xlabel('Classe')
plt.ylabel('Taux de survie')
plt.title('Taux de survie par classe')
plt.show()


# %%

# ### <font color='red'> EXERCISE : median by class </font>
# Perform a similar analysis with the median for the price per class in pounds.

# %%
plt.figure()
df_titanic.groupby('Pclass')['Fare'].aggregate(lambda x: x.median()).plot(kind='bar')
plt.show()

# ## Catplot, or a visual groupby

# %%

sns.catplot(x='Pclass', y="Age",
            hue="Sex", data=df_titanic_raw, kind="box", legend=False)
plt.title("Age par classe")
plt.legend(loc=1)
plt.tight_layout()

# %%
# Beware: large difference in sex ratio by class
df_titanic_raw.groupby(['Sex', 'Pclass'])[['Sex']].count()


# More on groupby pandas-kungfu: cf. also pd.crosstab, etc.
# https://pbpython.com/groupby-agg.html

# %%

# # Pandas: analyzing data with Python

# For data intensive work in Python, the Pandas library has become essential.
#
# What is pandas? It is an environment that manages Data Frame:
#
# - Pandas can handle *Data Frame* *numpy* tables with labels for rows and
# columns, and supports heterogeneous data types.
# - Pandas can also be considered as the data.frame of R in Python.
# - Powerful for working with missing data, working with time series data,
# reading and writing your data, reshaping, grouping, merging your data, ...

#
# Documentation: http://pandas.pydata.org/pandas-docs/stable/

# When are Pandas needed?
# When you work with tables or data structures (like dataframe R, SQL table,
# Excel, Spreadsheet, ...):
#
# - Import data
# - Cleaning "dirty" data
# - Explore and understand data
# - Process and prepare data for analysis
# - Analyze the data (with scikit-learn, statsmodels,...)
# <br/>
# <br/>
#
# **ATTENTION / LIMITS:**
#
# Pandas is good for working with heterogeneous data and 1D/2D tables, but not all data types fit into these structures!
#
# Counter-examples:
# - When working with **array** data (e.g. images): use *numpy*.
# - For labeled multidimensional data (e.g. climate data): see [xarray](http://xarray.pydata.org/en/stable/)

# # Data structures in pandas: DataFrame and Series

# A DataFrame is a tabular data structure (a multi-dimensional object that can contain labeled data) composed of rows and columns, similar to a spreadsheet, a database table, or R's data.frame object. You can think of it as several Series objects sharing the same index.


# %%

df_titanic


# %%

df_titanic.index


# %%

df_titanic.columns


# %%

pd.options.display.max_rows = 12
df_titanic.dtypes


# %%

df_titanic.info()


# %%

# Check that cabin is mostly missing, also the age
df_titanic_raw.info()


# %%

array_titanic = df_titanic.values  # associated numpy array
array_titanic


# ### <font color='red'> EXERCISE : dropna</font>
# Perform the following operation: remove the columns Cabin, and then remove the rows with missing age.
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
#

# %%

# XXX TODO

# %%




# # Données uni-dimensionel : Series (une colonne d'un DataFrame)

# Une Series est un support de base pour les données étiquetées unidimensionnelles.

# %%

fare = df_titanic['Fare']


# %%

fare


# ## Attributs de l'objet *Series*: indices et valeurs

# %%

fare.values[:10]


# %%

fare[6] # existe mais fare[0] provoque une erreur, car on l'a enlevé du dataFrame, comme valeur manquante.


# Contrairement au tableau *numpy*, cet index peut être autre chose qu'un entier:

# %%

df_titanic = df_titanic.set_index('Name')
df_titanic


# %%

age = df_titanic['Age']
age['Behr, Mr. Karl Howell']


# %%

age.mean()


# %%

df_titanic[age <2]


# %%

df_titanic_raw['Embarked'].value_counts()


# %%

pd.options.display.max_rows = 70
df_titanic[df_titanic['Embarked']=='C']  # Les passagers montés à Cherbourg n'ont pas des noms gaulois...


# %%

pd.options.display.max_rows = 8


# %%

df_titanic_raw['Survived'].sum() / df_titanic_raw['Survived'].count()


# %%

df_titanic['Survived'].mean()


# ** What was the proportion of women on the boat? **

# %%

# XXX TODO

# %%

df_titanic_raw.groupby(['Sex']).mean()


# # Data import et export
#
# Pandas supports nativement une large gamme de formats d'entrée / sortie:
# - CSV, text
# - SQL database
# - Excel
# - HDF5
# - json
# - html
# - pickle
# - sas, stata
# - ...

# %%

# pd.read_csv?


# # Exploration

# %%

df_titanic_raw.tail()


# %%

df_titanic_raw.head()


# %%

sns.set_palette("colorblind")
sns.catplot(x='Pclass',y='Age',hue='Survived',data=df_titanic_raw, kind="violin")


# %%

df_titanic_raw.columns


# # iloc

# %%

df_titanic.iloc[0:2,1:8]


# # loc

# %%

df_titanic.loc['Bonnell, Miss. Elizabeth', 'Fare']


# %%

df_titanic.loc['Bonnell, Miss. Elizabeth']


# %%

df_titanic.loc['Bonnell, Miss. Elizabeth','Survived']= 100


# %%

df_titanic.loc['Bonnell, Miss. Elizabeth']


# %%

df_titanic.loc['Bonnell, Miss. Elizabeth','Survived']= 1  # On remet la valeur comme avant


# # group-by:

# %%

df_titanic.groupby('Sex').mean()


# %%

df_titanic_raw.groupby('Sex').mean()['Pclass']  # attention ici on prend toutes les données, meme les manquantes...


# %%

df_titanic['AgeClass'] = pd.cut(df_titanic['Age'], bins=np.arange(0,90,10)) # créer des classes / découpes.


# %%

df_titanic['AgeClass']


# # Cas 2:  air quality in Paris.
# (Source: Airparif)
#

# %%

url = "http://josephsalmon.eu/enseignement/datasets/20080421_20160927-PA13_auto.csv"
path_target = "./20080421_20160927-PA13_auto.csv"
download(url, path_target, replace=False)


# %%

get_ipython().system('head -26 ./20080421_20160927-PA13_auto.csv')


# # Traitement des données temporelles et dates:
# https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html

# %%

polution_df = pd.read_csv('20080421_20160927-PA13_auto.csv', sep=';',
                          comment='#',
                          na_values="n/d",
                          converters={'heure': str})


# %%

polution_df.head(12)


# ## Preprocess the data

# ### <font color='red'> EXERCISE : handling missing values </font>
#
# What is the meaning of "na_values="n/d" above?
#
# Note that an alternative can be obtained with the command `polution_df.replace('n/d', np.nan, inplace=True)`
#

# %%

# check types
polution_df.dtypes


# For more info on the object nature (inherited from numpy), see https://stackoverflow.com/questions/21018654/strings-in-a-dataframe-but-dtype-is-object

# ### First issue non conventional hours

# %%

# start by changing to integer type (e.g. int8)
polution_df['heure'] = polution_df['heure'].astype(np.int8)

# no data is from 1 to 24... not conventional so let's make it from 0 to 23
polution_df['heure'] = polution_df['heure'] - 1

# and back to strings:
polution_df['heure'] = polution_df['heure'].astype('str')


# ### Time processing
#

# %%

# https://www.tutorialspoint.com/python/time_strptime.htm

time_improved = pd.to_datetime(polution_df['date'] +
                               ' ' + polution_df['heure'] + ':00',
                               format='%d/%m/%Y %H:%M')

# Where d = day, m=month, Y=year, H=hour, M=minutes


# %%

polution_df['date'] + ' ' + polution_df['heure'] + ':00'


# %%

time_improved


# %%

# create correct timing format in the dataframe
polution_df['DateTime'] = time_improved

# remove useles columns
del polution_df['heure']
del polution_df['date']


# %%

polution_df


# %%

# visualize the data set
polution_ts = polution_df.set_index(['DateTime'])
polution_ts = polution_ts.sort_index()
polution_ts.head(12)


# %%

polution_ts.describe()


# %%

fig, axes = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

axes[0].plot(polution_ts['O3'].resample('d').mean())
axes[0].set_title("Ozone polution: daily average in Paris")
axes[0].set_ylabel("Concentration (µg/m³)")

axes[1].plot(polution_ts['NO2'].resample('d').mean())
axes[1].set_title("Nitrogen polution: daily average in Paris")
axes[1].set_ylabel("Concentration (µg/m³)")

plt.show()


# ### <font color='red'> EXERCISE : worst of the day  </font>
# Provide the same plots as before, but with dayly best and worst on the same figures (use different colors)

# %%

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

axes[0].plot(polution_ts['O3'].resample('d').min(), label="O2(min)")
axes[0].plot(polution_ts['O3'].resample('d').max(), label="O2(max)")
axes[0].set_title("Ozone polution: daily min/max in Paris")
axes[0].set_ylabel("Concentration (µg/m³)")
axes[0].legend(loc=1)
axes[1].plot(polution_ts['NO2'].resample('d').min(), label="NO2(min)")
axes[1].plot(polution_ts['NO2'].resample('d').max(), label="NO2(max)")

axes[1].set_title("Nitrogen polution: daily min/max in Paris")
axes[1].set_ylabel("Concentration (µg/m³)")
axes[1].legend(loc=1)

plt.show()


# ### Is the polution getting better along the year?

# %%

ax = polution_ts['2008':].resample('A').mean().plot(figsize=(4,4))  # échantillone par année (A pour Annual)
plt.ylim(0,50)
plt.title("Evolution de la pollution: \n moyenne annuelle sur Paris")
plt.ylabel("Concentration (µg/m³)")
plt.xlabel("Années")


# %%

# Chargement des couleurs
sns.set_palette("GnBu_d", n_colors=7)
polution_ts['weekday'] = polution_ts.index.weekday  # Monday=0, Sunday=6

# polution_ts['weekend'] = polution_ts['weekday'].isin([5, 6])

days = ['Lundi', 'Mardi', 'Mercredi',
        'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

polution_week_no2 = polution_ts.groupby(['weekday', polution_ts.index.hour])[
    'NO2'].mean().unstack(level=0)
polution_week_03 = polution_ts.groupby(['weekday', polution_ts.index.hour])[
    'O3'].mean().unstack(level=0)
plt.show()


# %%




# %%

fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)

polution_week_no2.plot(ax=axes[0])
axes[0].set_ylabel("Concentration (µg/m³)")
axes[0].set_xlabel("Heure de la journée")
axes[0].set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes[0].set_xticks(np.arange(0, 24))
axes[0].set_xticklabels(np.arange(0, 24), rotation=45)
axes[0].set_ylim(0, 60)

polution_week_03.plot(ax=axes[1])
axes[1].set_ylabel("Concentration (µg/m³)")
axes[1].set_xlabel("Heure de la journée")
axes[1].set_title("Profil journalier de la pollution au O3: effet du weekend?")
axes[1].set_xticks(np.arange(0, 24))
axes[1].set_xticklabels(np.arange(0, 24), rotation=45)
axes[1].set_ylim(0, 70)
axes[0].legend().set_visible(False)
# ax.legend()
axes[1].legend(labels=days, loc='lower left', bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# %%

# XXX TODO quid des saisons?


# %%

import calendar
polution_ts['month'] = polution_ts.index.month  # Janvier=0, .... Decembre=11
polution_ts['month'] = polution_ts['month'].apply(lambda x: calendar.month_abbr[x])
polution_ts.head()


# %%

days = []

polution_month_no2 = polution_ts.groupby(['month', polution_ts.index.hour])[
    'NO2'].mean().unstack(level=0)
polution_month_03 = polution_ts.groupby(['month', polution_ts.index.hour])[
    'O3'].mean().unstack(level=0)


# %%

sns.set_palette("GnBu_d", n_colors=12)

fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)

polution_month_no2.plot(ax=axes[0])
axes[0].set_ylabel("Concentration (µg/m³)")
axes[0].set_xlabel("Heure de la journée")
axes[0].set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes[0].set_xticks(np.arange(0, 24))
axes[0].set_xticklabels(np.arange(0, 24), rotation=45)
axes[0].set_ylim(0, 90)

polution_month_03.plot(ax=axes[1])
axes[1].set_ylabel("Concentration (µg/m³)")
axes[1].set_xlabel("Heure de la journée")
axes[1].set_title("Profil journalier de la pollution au O3: effet du weekend?")
axes[1].set_xticks(np.arange(0, 24))
axes[1].set_xticklabels(np.arange(0, 24), rotation=45)
axes[1].set_ylim(0, 90)
axes[0].legend().set_visible(False)
# ax.legend()
axes[1].legend(labels=calendar.month_name[1:], loc='lower left', bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# # Your turn: explore the bike accident dataset
#
# https://www.data.gouv.fr/fr/datasets/accidents-de-velo-en-france/
#
# Possible visualisation
# https://koumoul.com/en/datasets/accidents-velos

# %%

url = "https://koumoul.com/s/data-fair/api/v1/datasets/accidents-velos/raw"
path_target = "./bicycle_db.csv"
download(url, path_target, replace=False)


# %%

# df: data frame
df_bikes = pd.read_csv("bicycle_db.csv", na_values="",
                       converters={'data': str, 'heure': str})


# %%

get_ipython().system('head -5 ./bicycle_db.csv')


# %%

pd.options.display.max_columns = 40
df_bikes.head()


# %%

df_bikes['existence securite'].unique()


# %%

df_bikes['gravite accident'].unique()


# ### Handle missing values in `heure`

# %%

df_bikes['date'].hasnans


# %%

df_bikes['heure'].hasnans


# %%

pd.options.display.max_rows = 20
df_bikes.iloc[400:402]


# %%

# remove missing hours cases by np.nan
df_bikes['heure']=df_bikes['heure'].replace('', np.nan)
df_bikes.iloc[400:402]


# %%

df_bikes.dropna(subset=['heure'], inplace=True)
df_bikes.iloc[399:402]


# ### <font color='red'> EXERCISE : Dates?  </font>
# Can you find the starting day and the ending day of the study automatically?
# hint sort the data.
# You can sort the data by time, , say with df.sort('Time') )

# %%

df_bikes['date'] + ' ' + df_bikes['heure'] + ':00'


# %%

# ADAPT OLD to create the df_bikes['Time']

time_improved = pd.to_datetime(df_bikes['date'] +
                               ' ' + df_bikes['heure'] + ':00',
                               format='%Y-%m-%d %H:%M')

# Where d = day, m=month, Y=year, H=hour, M=minutes
# create correct timing format in the dataframe


# %%

df_bikes['Time'] = time_improved
df_bikes.set_index('Time',inplace=True)
# remove useles columns
del df_bikes['heure']
del df_bikes['date']


# %%

df_bikes.info()


# %%

df_bikes_partial = df_bikes[['gravite accident', 'existence securite', 'age', 'sexe']]
df_bikes_partial['existence securite'] = df_bikes_partial['existence securite'].replace(np.nan, "Inconnu")
df_bikes_partial.dropna(inplace=True)


# ### <font color='red'> EXERCISE : Is the helmet saving your life?  </font>
# Peform an analysis so that you can check the benefit or not of wearing helmet to save your life.
# Beware preprocessing needed to use `pd.crosstab`,  `pivot_table` to avoid issues.

# %%

group = df_bikes_partial.pivot_table(columns='existence securite',index=['gravite accident','sexe'], aggfunc={'age': 'count'}, margins=True)
group


# %%

# pd.crosstab?
pd.crosstab(df_bikes_partial['existence securite'], df_bikes_partial['gravite accident'], normalize='index') *100


# %%

pd.crosstab(df_bikes_partial['existence securite'], df_bikes_partial['gravite accident'], values = df_bikes_partial['age'], aggfunc='count', normalize='index') *100


# ### <font color='red'> EXERCISE : Are men and women dying equally on a bike?  </font>
# Peform an analysis to check any difference between men and woman survival on a bike?

# %%

idx_dead = df_bikes['gravite accident']=='3 - Tué'
df_deads = df_bikes[idx_dead]
df_gravite = df_deads.groupby('sexe').size() / idx_dead.sum()
df_gravite


# %%

df_bikes.groupby('sexe').size()  / df_bikes.shape[0]


# %%

pd.crosstab(df_bikes_partial['sexe'], df_bikes_partial['gravite accident'], values = df_bikes_partial['age'], aggfunc='count', normalize='columns',margins=True)*100


# ### To conclude:
# some information on the level of bike practice by men/women is missing... though

# ### <font color='red'> EXERCISE : Accident during the week?  </font>
# Peform an analysis to check when the accidents are occuring during the week.

# %%

df_bikes


# %%

# Chargement des couleurs
sns.set_palette("colorblind", n_colors=7)
df_bikes['weekday'] = df_bikes.index.weekday  # Monday=0, Sunday=6

days = ['Lundi', 'Mardi', 'Mercredi',
        'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

accidents_week = df_bikes.groupby(['weekday', df_bikes.index.hour])[
    'sexe'].count().unstack(level=0)

fig, axes = plt.subplots(1, 1, figsize=(7, 7))


accidents_week.plot(ax=axes)
axes.set_ylabel("Accidents")
axes.set_xlabel("Heure de la journée")
axes.set_title(
    "Profil journalier des accidents: effet du weekend?")
axes.set_xticks(np.arange(0, 24))
axes.set_xticklabels(np.arange(0, 24), rotation=45)
# axes.set_ylim(0, 6)
axes.legend(labels=days, loc='lower left', bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# %%

df_bikes.groupby(['weekday', df_bikes.index.hour])[
    'sexe'].count()


# ### <font color='red'> EXERCISE : Accident during the year?  </font>
# Peform an analysis to check when the accidents are occuring during the week.

# %%


import calendar
df_bikes['month'] = df_bikes.index.month  # Janvier=0, .... Decembre=11
df_bikes['month'] = df_bikes['month'].apply(lambda x: calendar.month_abbr[x])
df_bikes.head()

sns.set_palette("GnBu_d", n_colors=12)
# sns.set_palette("colorblind", n_colors=12)

df_bikes_month = df_bikes.groupby(['month', df_bikes.index.hour])[
    'age'].count().unstack(level=0)

fig, axes = plt.subplots(1, 1, figsize=(7, 7), sharex=True)

df_bikes_month.plot(ax=axes)
axes.set_ylabel("Concentration (µg/m³)")
axes.set_xlabel("Heure de la journée")
axes.set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes.set_xticks(np.arange(0, 24))
axes.set_xticklabels(np.arange(0, 24), rotation=45)
# axes.set_ylim(0, 90)
axes.legend(labels=calendar.month_name[1:], loc='lower left', bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# ### <font color='red'> EXERCISE : Accidents by departement  </font>
# Peform an analysis to check when the accidents are occuring by departement.

# %%

import pygal  
# First install if needed for maps:
# pip install pygal
# andpip install pygal_maps_frpip install pygal_maps_fr
# pip install pygal_maps_fr

# Departement population: https://public.opendatasoft.com/explore/dataset/population-francaise-par-departement-2018/table/?disjunctive.departement&location=7,47.12995,3.41125&basemap=jawg.streets
path_target = "./dpt_population.csv"
url = "https://public.opendatasoft.com/explore/dataset/population-francaise-par-departement-2018/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
download(url, path_target, replace=False)

# %%
# Departement area: https://www.regions-et-departements.fr/departements-francais#departements_fichiers
path_target = "./dpt_area.csv"
url = "https://www.regions-et-departements.fr/fichiers/departements-francais.csv"
download(url, path_target, replace=False)

df_dtp_pop = pd.read_csv("dpt_population.csv", sep=";", low_memory=False)
df_dtp_area = pd.read_csv("dpt_area.csv", sep="\t", low_memory=False, skiprows=[102, 103, 104])
df_dtp_area['NUMÉRO']


df_dtp_area.set_index('NUMÉRO', inplace=True)

df_dtp_pop.set_index('Code Département', inplace=True)
df_dtp_pop.sort_index(inplace=True)


fr_chart = pygal.maps.fr.Departments(human_readable=True)

# display = "ration_tue"
display = "ratio_accident"


if display is "ratio_accident":
    fr_chart.title = 'Accidents by departement'
    gd = df_bikes.groupby(['departement']).size()
    gd = (gd / df_dtp_pop['Population'])  # mean accident per habitant
else:
    fr_chart.title = 'Deaths by departement'
    df_deads = df_bikes[df_bikes['gravite accident']=='3 - Tué']
    df_gravite = df_deads.groupby('departement').size()
    # gd = df_bikes.groupby(['departement']).aggregate(lambda: x->sum(x))
    gd = (df_gravite / df_dtp_pop['Population'])  # mean deaths per habitant

# Area normalization
normalization = True
if normalization is True:
    gd = (gd / df_dtp_area['SUPERFICIE (km²)'])
gd.dropna(inplace=True)   # anoying NA due to 1 vs 01 in datasets
fr_chart.add('Accidents', gd.to_dict())
fr_chart.render_in_browser()
# fr_chart.render_to_file('./chatr.svg')  # Write the chart in a specified file
