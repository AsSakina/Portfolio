#Importing Needed Packages

import chart_studio.tools as tls
import numpy as np
import pandas as pd
#import pandas_profiling as pp
import matplotlib.pyplot as mp
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

data = pd.read_csv('Mental health Depression disorder Data 2.csv', low_memory=False)
data 

#fig = px.scatter(x=range(10), y=range(10))
#fig.write_html("path/to/file.html")
#tls.get_embed('https://plotly.com/~chris/1638')
#fig = px.scatter(x=range(10), y=range(10))
#fig.write_html("path/to/file.html")

#Get Informations using info()
data.info()

#Get first rows using head()
data.head()

#Describing our DataSet using Describe()
data.describe()

#List the number of missing values for each column
print('N° Missing values for columns : ')
print('Schizophrenia :', data['Schizophrenia (%)'].isna().sum())
print('Bipolar disorder :', data['Bipolar disorder (%)'].isna().sum())
print('Eating disorders :', data['Eating disorders (%)'].isna().sum())
print('Anxiety disorders :', data['Anxiety disorders (%)'].isna().sum())
print('Drug use disorders :', data['Drug use disorders (%)'].isna().sum())
print('Depression :', data['Depression (%)'].isna().sum())
print('Alcohol use disorders :', data['Alcohol use disorders (%)'].isna().sum())

#we can notice that missing values are almost all found on the same lines
data[data['Bipolar disorder (%)'].isna()]

#we can notice that missing values are almost all found on the same lines
data[data['Eating disorders (%)'].isna()]

'''  Observations

On remarque qu'il y a beaucoup de valeurs manquantes dans les colonnes : Code; Schizophrenia (%); Bipolar disorder (%); Eating disorders (%); Anxiety disorders (%); Drug use disorders (%); Depression (%); Alcohol use disorders (%)
A partir de l'index 6468 de nouvelles colonnes y sont présentes
A partir de l'index 54278 de nouvelles colonnes aussi
De même qu'à partir de l'index 102084 de nouvelles colonnes y sont.
To Do

Copie de notre dataset pour le garder intact
Supression de la colonne Index parce qu'on a déjà des identifiants uniques
Gestion des valeurs manquantes
Gestion des nouvelles colonnes  '''


#Copy de notre DataSet
#Copying our dataset
_data = data.copy()

#Suppression de la Colonne Index
#Deleting Index column

#data.dropna(['index'], axis=1, inplace=True)
#data.head()

#Gestion des Colonnes** : Afficher toutes les colonnes existantes de notre Dataset
#Handling Columns 

#First by spilling tables and naming the headers based on columns 
data_1 = data.iloc[:6467]

data_2 = data.iloc[6469:54276]
data_2.columns = data.iloc[6468]
data_2 = data_2.iloc[:,:7].drop(columns = 6468)

data_3 = data.iloc[54277:102084]
data_3.columns = data.iloc[54276]
data_3 = data_3.iloc[:,:7].drop(columns = 54276)

data_4 = data.iloc[102085:]
data_4.columns = data.iloc[102084]
data_4 = data_4.iloc[:,:5].drop(columns = 102084)

#Joining tables based on entity, code and year for a deeper analysis

Tab1 =pd.merge(data_1, data_2, how='left', on=['Entity', 'Code', 'Year'])
Tab2 = pd.merge(Tab1, data_3, how='left', on=['Entity', 'Code', 'Year'])
_data = pd.merge(Tab2, data_4, how='left', on=['Entity', 'Code', 'Year'])
_data.head()
Tab2

#Gestion des Valeurs manquantes 
''' Supression des lignes avec des valeurs manquantes puisqu'elles se trouvent sur les mêmes lignes de toutes les colonnes. '''

#Handling Missing Values

#Drop NaN rows
_data.dropna(axis=0, how='any', inplace=True)
_data.head()

#Drop NaN rows 
_data.dropna(axis=0, how='any', inplace=True)

#We can notice that missing values are almost all found on the same lines
_data[_data['Eating disorders (%)'].isna()]
#We can notice that missing values are almost all found on the same lines
_data[_data['Bipolar disorder (%)'].isna()]

#Rename our Dataset
_data.to_csv(r'Psychological Disorder.csv', index=False)

# Check our dataset after dropping NaN
_data.info()

#Changing type to float
_data['Schizophrenia (%)'] = _data['Schizophrenia (%)'].astype(float)
_data['Prevalence in females (%)'] = _data['Prevalence in females (%)'].astype(float)
_data['Prevalence in males (%)'] = _data['Prevalence in males (%)'].astype(float)
_data['Population_x'] = _data['Population_x'].astype(float)
_data['Depressive disorder rates (number suffering per 100,000)'] = _data['Depressive disorder rates (number suffering per 100,000)'].astype(float)
_data['Population_y'] = _data['Population_y'].astype(float)
_data['Prevalence - Depressive disorders - Sex: Both - Age: All Ages (Number) (people suffering from depression)'] = _data['Prevalence - Depressive disorders - Sex: Both - Age: All Ages (Number) (people suffering from depression)'].astype(float)
_data['Bipolar disorder (%)'] = _data['Bipolar disorder (%)'].astype(float)
_data['Eating disorders (%)'] = _data['Eating disorders (%)'].astype(float)
_data['Anxiety disorders (%)'] = _data['Anxiety disorders (%)'].astype(float)
_data['Suicide rate (deaths per 100,000 individuals)'] = _data['Suicide rate (deaths per 100,000 individuals)'].astype(float)

_data.info()

