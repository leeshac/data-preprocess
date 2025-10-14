import pandas as pd
import numpy as np

#function to replace missing values with mode
def replace_missing_with_mode(data):
    mode_val = data.mode()[0]
    return data.fillna(mode_val)

#function to convert ordinal data to numerical data using set mapping
def ordinal_encoding(data, mapping):
    data = data.map(mapping)
    return data

#main function
def categorical_ordinal_preprocess(dataframe, column_name, mapping):
    dataframe = dataframe.copy() #to avoid modifying original dataframe
    data = dataframe[column_name] #select the column to preprocess
    
    data = replace_missing_with_mode(data)
    data = ordinal_encoding(data, mapping)
    
    dataframe[column_name] = data #update the column in the dataframe
    return dataframe, mapping #return the modified dataframe and the mapping dictionary