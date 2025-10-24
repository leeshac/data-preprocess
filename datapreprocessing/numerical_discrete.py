import pandas as pd
import numpy as np

#STEPS:
#1. replace missing values with median
#2. remove outliers with clipping IQR
#3. return the modified dataframe

#function to replace missing values with median
def replace_missing_with_median(data):
    median_val = data.median()
    return data.fillna(median_val)

#function to remove outliers with clipping IQR
#TODO: clipping can produce floats so may need to round
def removee_outliers_iqr(data):
    Q1 = data.quantile(0.25) #first quartile
    Q3 = data.quantile(0.75) #third quartile
    IQR = Q3 - Q1 #interquartile range
    lower_bound = Q1 - 1.5 * IQR #calc lower bound
    upper_bound = Q3 + 1.5 * IQR #calc upper bound
    return data.clip(lower=lower_bound, upper=upper_bound) #clip values outside bounds

#main function to call the above functions
def numerical_discrete_preprocess(dataframe, column_name): #specify column name to preprocess
    dataframe = dataframe.copy() #to avoid modifying original dataframe
    data = dataframe[column_name] #select the column to preprocess
    data = replace_missing_with_median(data)
    data = removee_outliers_iqr(data)
    dataframe[column_name] = data #update the column in the dataframe
    return dataframe