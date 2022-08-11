#!/usr/bin/env python
# coding: utf-8

# # Trabajo Estadistica G4
# # Uso de internet global
# 

# # Caracteristicas
# 1. Ingresos percibidos
# 1. Usuarios de internet
# 1. Grado de Urbanizacion

# # Contenido
# 1. Carga y comprobación de datos
# 1. Visualización de datos
# 1. Ingeniería de características
# 1. Modelado
# 1. Estandarización
# 1. *Metodo Usado*

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# # 1. Carga y comprobación de datos

# In[11]:


data.columns


# In[2]:


data = 'https://raw.githubusercontent.com/FernandoZacVal/dataset/main/gapminder_internet.csv'
data = pd.read_csv(data)


# In[3]:


data.head()


# In[4]:


data.shape


# In[9]:


data.info()


# In[5]:


data.iloc[:,0:4].head().describe().T


# # 2. Visualización de datos

# In[14]:


plt.subplots(figsize=(6, 8))

sns.set_color_codes("pastel")
sns.barplot(x="income/person", y="country", data=data.sort_values(ascending=False, by="income/person").head(30), 
            color="b").set(ylabel=None)

plt.show()


# In[19]:


plt.subplots(figsize=(10, 6))

sns.lineplot(y="income/person", x="urban_rate", data=data, label="urban_rate").set(xlabel=None)
sns.lineplot(y="income/person", x="internet_usage", data=data, label="internet_usage").set(xlabel=None)

plt.legend()
plt.show()


# In[7]:


fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(data.corr(), annot=True, fmt=".2f" , ax=ax , cmap= "Blues")
plt.show()


# In[25]:


sns.pairplot(data, hue="income/person")
plt.show()


# In[26]:


sns.pairplot(data, hue="urban_rate")
plt.show()


# In[27]:


sns.pairplot(data, hue="internet_usage")
plt.show()


# In[23]:


plt.boxplot(data["urban_rate"])
plt.show()


# In[28]:


plt.boxplot(data["income/person"])
plt.show()


# In[ ]:




