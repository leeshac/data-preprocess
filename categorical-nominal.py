import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#STEPS:
#1. replace missing values with mode
#2. encode the nominal values using label encoding for tree based models and one hot encoding for relation based models
#3. return the modified dataframe and the mapping dictionary if label encoding is used

#function to replace missing values with mode
def replace_missing_with_mode(data):
    mode_val = data.mode()[0]
    return data.fillna(mode_val)

#function to convert categorical nominal data to numerical data - tree based models
def label_encoding(data):
    le = LabelEncoder()
    data = le.fit_transform(data)
    return data, dict(zip(le.classes_, le.transform(le.classes_)))
#return the modified dataframe and the hashmap for reference

#function to convert categorical nominal data to numerical data - relation based models
def one_hot_encoding(data):
    unique_vals = data.unique()
    one_hot_df = pd.DataFrame(0, index=data.index, columns=[f"{data.name}_{val}" for val in unique_vals])
    #the above line creates a df with 0s and columns for each unique val in the original columns by.

    for val in unique_vals:
        one_hot_df.loc[data == val, f"{data.name}_{val}"] = 1 #set 1 where the value matches
    return one_hot_df

#main function
def categorical_nominal_preprocess(dataframe, column_name, model_type):
    dataframe = dataframe.copy() #to avoid modifying original dataframe
    data = dataframe[column_name] #select the column to preprocess
    
    data = replace_missing_with_mode(data)

    #TODO: might change this 
    if model_type == 'tree_based':
        data, mapping = label_encoding(data)
        dataframe[column_name] = data #update the column in the dataframe
        return dataframe, mapping #return the modified dataframe and the mapping dictionary
    else:
        data = one_hot_encoding(data)
        dataframe[column_name] = data #update the column in the dataframe
        return dataframe 
    
    #TODO: add handling for missing values if needed