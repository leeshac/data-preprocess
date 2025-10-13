import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#function to replace missing values with median
def replace_missing_with_median(data):
    median_val = data.median()
    return data.fillna(median_val)

#function to remove outliers with clipping IQR
def remove_outliers_iqr(data):
    Q1 = data.quantile(0.25) #first quartile
    Q3 = data.quantile(0.75) #third quartile
    IQR = Q3 - Q1 #interquartile range
    lower_bound = Q1 - 1.5 * IQR #calc lower bound
    upper_bound = Q3 + 1.5 * IQR #calc upper bound
    return data.clip(lower=lower_bound, upper=upper_bound) #clip values outside bounds

#function to transform data with log1p
#TODO: may modify to use boxcox if needed
def transform_data_log1p(data):
    return np.log1p(data) #log1p helps stabilize skewed distributions and handle zeros

#function to scale data with standard scaler
def scale_data_standardscaler(data):
    scaler = StandardScaler()
    #we need to reshape and flatten the data to fit the scaler and map it back to dataframe
    #standard scaler expects 2D array so we reshape to (-1,1) and then flatten back to 1D for dataframe column assignment
    data = scaler.fit_transform(data.values.reshape(-1, 1).flatten()) #reshape and flatten so it can be mappped back to dataframe 
    return data

#main function to call the above functions
def numerical_continuous_preprocess(dataframe, column_name): #specify column name to preprocess
    dataframe = dataframe.copy() #to avoid modifying original dataframe
    data = dataframe[column_name] #select the column to preprocess
    data = replace_missing_with_median(data)
    data = remove_outliers_iqr(data)
    data = transform_data_log1p(data)
    data = scale_data_standardscaler(data)
    dataframe[column_name] = data #update the column in the dataframe
    return dataframe