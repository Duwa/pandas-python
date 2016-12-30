# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:08:21 2016
COntext of the problem: Pandas Data frame manipulation for 
@author: duwarahan
"""
import os
import glob
import pandas as pd
import numpy as np
import re
import decimal
from decimal import Decimal
# get data file names
path =r'wx_data'
filenames = glob.glob(path + "/*.txt")

# Problem#1
list_of_records = []
list_of_files = []
dfs = []
for filename in filenames:
    df = pd.read_csv(filename,sep = '\t', header = None)
    temp_data = df.ix[(df[2] != -9999) & (df[1] != -9999) & (df[3] == -9999) ]
    number_of_records  = len(temp_data.index)
    file_name1 = re.compile(r'(U).*', re.VERBOSE)
    file = file_name1.search(filename).group()
    list_of_records.append(number_of_records)
    list_of_files.append(file)
    dfs.append(df)
    
Problem1_dataframe = pd.DataFrame({'file_name' : list_of_files,
                                    'number_of_records' : list_of_records})

df4 = Problem1_dataframe.sort('file_name')
df4.to_csv('MissingPrcpData.out.txt', sep = '\t', index = False)

#problem#2
list_of_files = []
Averagemaximumtemperature1 = []
Averageminimumtemperature1 = []
Totalaccumulatedprecipitation1 = []
year1 = []
for filename in filenames:
    df = pd.read_csv(filename,sep = '\t', header = None)
    for i in range(1985,2015):
       df[0] = df[0].astype(int).astype('str')
       data_mung =  df[df[0].str.contains(str(i))]
       data_mung.replace(-9999, 0, inplace = True)
       Averagemaximumtemperature = data_mung[1].mean()
       d1 = Decimal(str(Averagemaximumtemperature)).quantize(Decimal('0.01'))  
       Averageminimumtemperature = data_mung[2].mean()
       d2 = Decimal(str(Averageminimumtemperature)).quantize(Decimal('0.01'))
       Totalaccumulatedprecipitation = data_mung[2].sum()
       d3 = Decimal(str(Totalaccumulatedprecipitation)).quantize(Decimal('0.01'))
       year = i
       file_name1 = re.compile(r'(U).*', re.VERBOSE)
       file = file_name1.search(filename).group()
       list_of_files.append(file)
       Averagemaximumtemperature1.append(d1)
       Averageminimumtemperature1.append(d2)
       Totalaccumulatedprecipitation1.append(d3)
       year1.append(year)
       
Problem2_dataframe = pd.DataFrame({'file_name' : list_of_files,
                                    'year' : year1,
                                    'Average_maximum_temperature' : Averagemaximumtemperature1,
                                    'Average_minimum_temperature' : Averageminimumtemperature1,
                                    'Total_accumulated_precipitation':Totalaccumulatedprecipitation1 })


df3 = Problem2_dataframe.sort('file_name')
df3.to_csv('YearlyAverages.out.txt', sep = '\t', index = False)

year12 = []
file_count = []

for file in Problem2_dataframe['file_name']:
    df =  Problem2_dataframe[Problem2_dataframe['file_name'].str.contains(file)]    
    year_ = df.loc[df['Average_maximum_temperature'].idxmax()][4]
    year12.append(year_)
    file_count.append(file)
    
df12 = pd.DataFrame({'year' : year12,
                                    'file' : file_count })   
    
X = df12.groupby('year').size()
    
for file in Problem2_dataframe['file_name']:
    df =  Problem2_dataframe[Problem2_dataframe['file_name'].str.contains(file)]    
    year_ = df.loc[df['Average_minimum_temperature'].idxmax()][4]
    year12.append(year_)
    file_count.append(file)

df13 = pd.DataFrame({'year' : year12,
                                    'file' : file_count })     

Y = df13.groupby('year').size()

for file in Problem2_dataframe['file_name']:
    df =  Problem2_dataframe[Problem2_dataframe['file_name'].str.contains(file)]    
    year_ = df.loc[df['Total_accumulated_precipitation'].idxmax()][4]
    year12.append(year_)
    file_count.append(file)    

df14 = pd.DataFrame({'year' : year12,
                                    'file' : file_count })       
   
Z = df14.groupby('year').size()


x = df.loc[df['Average_maximum_temperature'].idxmax()][4]
dataframe_ = pd.concat([X,Y,Z], axis=1)

dataframe_.rename(columns={0: "Average_maximum_temperature", 1: "Average_minimum_temperature", 2: "Total_accumulated_precipitation"}, inplace = True)
# Histogram and output file
dataframe_[['Average_maximum_temperature', 'Average_minimum_temperature','Total_accumulated_precipitation']].plot.hist(alpha=0.5, bins=20)
dataframe_.to_csv('YearHistogram.out.txt', sep = '\t')

# problem # 4

df = pd.read_csv('US_corn_grain_yield.txt',sep = '\t', header = None)

corr_mat = Problem2_dataframe[Problem2_dataframe.columns[2]].apply(lambda x: x.corr(df[1]))

sLength = len(Problem2_dataframe['year'])

final_mat['yield'] = final_mat['yield'].astype(int).astype(ob)

list_of_files = []
Averagemaximumtemperature1 = []
Averageminimumtemperature1 = []
Totalaccumulatedprecipitation1 = []
year1 = []
for filename in filenames:
    df = pd.read_csv(filename,sep = '\t', header = None)
    for i in range(1985,2015):
       df[0] = df[0].astype(int).astype('str')
       data_mung =  df[df[0].str.contains(str(i))]
       data_mung.replace(-9999, 0, inplace = True)
       Averagemaximumtemperature = data_mung[1].mean()
       Averageminimumtemperature = data_mung[2].mean()
       Totalaccumulatedprecipitation = data_mung[2].sum()
       year = i
       file_name1 = re.compile(r'(U).*', re.VERBOSE)
       file = file_name1.search(filename).group()
       list_of_files.append(file)
       Averagemaximumtemperature1.append(Averagemaximumtemperature)
       Averageminimumtemperature1.append(Averageminimumtemperature)
       Totalaccumulatedprecipitation1.append(Totalaccumulatedprecipitation)
       year1.append(year)
       
Problem4_dataframe = pd.DataFrame({'file_name' : list_of_files,
                                    'year' : year1,
                                    'Average_maximum_temperature' : Averagemaximumtemperature1,
                                    'Average_minimum_temperature' : Averageminimumtemperature1,
                                    'Total_accumulated_precipitation':Totalaccumulatedprecipitation1 })
                                    
final_mat = Problem4_dataframe.merge(df, on = 'year' , how = 'left')
Y = final_mat.groupby('file_name').corr() 
Y.to_csv('Correlations.out.txt', sep = '\t')
