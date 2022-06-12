#!/usr/bin/env python
# coding: utf-8

# # Graded Challenge 1
# 
# `MARWAN MUSA - BATCH 12`

# ## Description
# 
# ### Objective
# 
# I'm an employee at a new start-up - mobile gaming company, we are building a monster game that likely will have the same visual and experience with a pokemon game. My division's job is to get some specific information from a pokemon dataset that has been spread across the internet, in order to improve our monster figure in our own game.
# 
# ### Problem Statements
# 
# My duties are:
# - To find out the dominant strength of each pokemon type.
# - To classify the pokemons' power difference by the strongest and the weakest of *legendary* and *non-legendary* type.
# - To find out the pokemons' hit points, speed, and total power differences by its *generation*.

# ## Working Area

# ### ***Importing Module***

# In[92]:


import numpy as np
import pandas as pd


# ---

# ### ***Loading Data***

# In[93]:


df = pd.read_csv('Pokemon.csv')
df


# ---

# ### ***Cleaning Data***

# We will update the name of some columns, in order to make it easy to use.

# In[94]:


pokemon = df.rename(
    columns={"Type 1": "Type_1", "Type 2": "Type_2", "Sp. Atk": "Sp_Atk", "Sp. Def": "Sp_Def"}
)
pokemon


# In[95]:


pokemon.info()


# It seems like the column of *"type 2"* doesn't have the same value with the total entries, where it should be 800 data in it, but *"type 2"* just have 414 data.

# Replacing NaN values in *type 2* column with string value "No Type"

# In[96]:


pokemon[['Type_2']] = pokemon[['Type_2']].fillna('No Type')
pokemon


# In[97]:


pokemon.info()


# It can be seen that the dataset has no missing value.

# ---

# ### ***Exploring the Dataset***

# >How many of them are *single type* or *dual type* pokemon?

# We can find it by filtering *Type_2* column that has "No Type" value

# In[98]:


pokemon[pokemon.Type_2 == 'No Type']


# Based on table above, we can conclude that 386 pokemons are *single type* because they don't have a second power and the rest are *dual type*. 

# >What is the dominant strength of each pokemon's type?

# In[99]:


pokemon.Type_1.value_counts()


# *Water* strength is the most common ability that pokemons have in type 1.

# In[100]:


pokemon[pokemon['Type_2'] != 'No Type'].Type_2.value_counts()


# *Flying* strength is the most common ability that pokemons have in type 2.

# >How many pokemons are *legendary* and *non legendary*?

# In[101]:


pokemon.Legendary.value_counts()


# We can see that 65 pokemons are *legendary* and 735 are *non-legendary*.

# >Total power of *legendary* and *non-legendary* pokemon

# #### **Legendary**

# In[102]:


pokemon[pokemon['Legendary'] == True].Total.agg(('min','max'))


# - The strongest legendary pokemon has 780 total power, and
# - The weakest legendary pokemon has 580 total power.

# Here they are:

# In[103]:


pokemon[
    (pokemon["Legendary"] == True) &
    (pokemon["Total"] == 580)
]

# the weakest legendary pokemons


# In[104]:


pokemon[
    (pokemon["Legendary"] == True) &
    (pokemon["Total"] == 780)
]

# the strongest legendary pokemons


# #### **Non-Legendary**

# In[105]:


pokemon[pokemon['Legendary'] == False].Total.agg(('min','max'))


# - The strongest non-legendary pokemon has 700 total power, and
# - The weakest non-legendary pokemon has 180 total power.

# Here they are:

# In[106]:


pokemon[
    (pokemon["Legendary"] == False) &
    (pokemon["Total"] == 180)
]

# the weakest non-legendary pokemons


# In[107]:


pokemon[
    (pokemon["Legendary"] == False) &
    (pokemon["Total"] == 700)
]

# the strongest non-legendary pokemons


# >HP, Speed and Total power by pokemon's generation

# #### **Hit Points**

# In[108]:


pokemon.groupby("Generation", sort=False)["HP"].max()


# #### **Speed**

# In[109]:


pokemon.groupby("Generation", sort=False)["Speed"].max()


# #### **Total Power**

# In[110]:


pokemon.groupby("Generation", sort=False)["Total"].agg(('min','max'))


# Have a look at the *hp*, *speed* and *total power* data above in a different way:

# #### **Hit Points**

# In[111]:


pokemon.groupby("Generation", sort=False)["HP"].max().plot(
    kind = 'bar', 
    color = 'seagreen', 
    title = 'Maximum HP for Each Generation',
    ylabel = 'Hit Points')


# #### **Speed**

# In[112]:


pokemon.groupby("Generation", sort=False)["Speed"].max().plot(
    kind = 'bar', 
    color = 'royalblue', 
    title = 'Maximum Speed for Each Generation',
    ylabel = 'Speed')


# #### **Total Power**

# In[113]:


pokemon.groupby("Generation", sort=False)["Total"].agg(('min','max')).plot(
    kind = 'bar', 
    title = 'The Highest and The Lowest Total Power for Each Generation',
    ylabel = 'Total Power')


# ## Conclusions, Assumptions, Overall Analysis

# In accordance with the result, it is found that:
# - the dominant strength of pokemons' *first power* is *water strength*, and if they have second power or if they are *dual type pokemon*, then most of them are *flying pokemons*.
# 
# - The strongest *legendary* and *non-legendary* type has only 80 points difference of their total power value. The total power of the strongest *legendary* and *non-legendary* pokemon is 780 and 700 respectively. While The weakest *legendary* and *non-legendary* type is up to 400 points difference of their total power value. The total power of the weakest *legendary* and *non-legendary* pokemon is 580 and 180 respectively.
# 
# - According to the generations, 
# 1. Most pokemons with the highest damage resistance based on their hit points are from the *first* and *second generation* with only 5 points difference.
# 2. The fastest pokemon based on their speed is found in the *third generation*.
# 3. The *most powerful* pokemons are from the *first* and *third generation*. It can be seen from the highest value of the total power of all generation is found in the *first* and *third generation*. Otherwise, the *most delicate* pokemon is from the *second generation*. 
#  
