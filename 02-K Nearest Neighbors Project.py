#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[2]:


import pandas as pd
import numpy as np


# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# **Check the head of the dataframe.**

# In[9]:


df=pd.read_csv('KNN_Project_Data')
df.head()


# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[10]:


sns.pairplot(df,hue='TARGET CLASS', palette='coolwarm')


# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[13]:


from sklearn.preprocessing import StandardScaler


# ** Create a StandardScaler() object called scaler.**

# In[14]:


scaler=StandardScaler()


# ** Fit scaler to the features.**

# In[15]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# **Use the .transform() method to transform the features to a scaled version.**

# In[16]:


scaled_features=scaler.transform(df.drop('TARGET CLASS',axis=1))


# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[18]:


df_feat=pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat


# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[20]:


from sklearn.model_selection import train_test_split


# In[22]:


train_test_split


# In[27]:


X=df_feat
y=df['TARGET CLASS']


# In[28]:



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[29]:


from sklearn.neighbors import KNeighborsClassifier


# **Create a KNN model instance with n_neighbors=1**

# In[30]:


knn=KNeighborsClassifier(n_neighbors=1)


# **Fit this KNN model to the training data.**

# In[31]:


knn.fit(X_train,y_train)


# # Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[32]:


pred=knn.predict(X_test)


# ** Create a confusion matrix and classification report.**

# In[33]:


from sklearn.metrics import classification_report,confusion_matrix


# In[36]:


print(confusion_matrix(y_test,pred))


# In[37]:


print(classification_report(y_test,pred))


# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# In[40]:


error_rate=[]
for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i=knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
    


# **Now create the following plot using the information from your for loop.**

# In[43]:


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='--',marker='o',markerfacecolor='red',markersize=10)
plt.title('Error Rate vs K')
plt.xlabel('K')
plt.ylabel('Error Rate')


# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[46]:


knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# # Great Job!
