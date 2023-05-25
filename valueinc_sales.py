# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:18:18 2023

@author: Shikhar Mehra
"""
import pandas as pd

# file_name = pd.read_csv('file.csv') <-- format to read csv

#data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv' , sep=';')
# initdata=data
 #summary of the data 
# data.info()

#working with calculations

#defining variables

# CostPerItem = 11.75
# SellPricePerItem = 21.11
# NumberOfItemspurchased = 6

# ProfitPerItem = 21.11-11.73
# ProfitPerItem = SellPricePerItem-CostPerItem

# ProfitPerTransaction = NumberOfItemspurchased*ProfitPerItem
# CostPerTransaction = NumberOfItemspurchased*CostPerItem
# SellingPricePerTransaction = NumberOfItemspurchased*SellPricePerItem

CostPerItem = data['CostPerItem']
NumberOfItemspurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemspurchased 

#adding a column to dataframe
data['CostPerTransaction'] = CostPerTransaction

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#ProfitPerTransaction = sales - cost
data['ProfitPertransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup = (sales-cost)/cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']

data['Markup'] = (data['ProfitPertransaction'])/data['CostPerTransaction']

#rounding markup
roundmarkup = round(data['Markup'],2) 
data['Markup'] = round(data['Markup'],2)

#combining data fields 
#simple concatenation
my_date = 'Day'+'-'+'Month'+'-'+'Year'


#checking data type
#print(data['Day'].dtype)

#changing datatype of column
day = data['Day'].astype(str)
year = data['Year'].astype(str)
#print(day.dtype)
#print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specif columns/rows
#data.iloc[0] #view row with index 0
#data.iloc[0:3] #view 0 to 3 rows
#data.iloc[-5:] #view last 5 rows
#data.head(5)#view first 5 rows
data.iloc[:,2] #view all rows on 2nd column
#data.iloc[4,2] #view 4th row , 2nd column


#using split to split client keyword field
#new_var = column.str.split('sep' , expand = True)
split_col = data['ClientKeywords'].str.split(',',expand = True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace function 
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#converting uppercase to lowercase
data['ItemDescription'] =  data['ItemDescription'].str.lower()


#how to merge files
#bringing in a new data set
seasons = pd.read_csv('value_inc_seasons.csv' , sep=';')

#merging files: merge_df = pd.merge(df_old, df_new , on = 'key')
data = pd.merge(data, seasons, on='Month')

#dropping columns
#DF = DF.DROP('COLUMNNAME' , AXIS = 1)
data = data.drop('ClientKeywords',axis=1)
data = data.drop('Day',axis=1)
data = data.drop(['Year','Month'],axis=1)

#export into a csv 
data.to_csv('ValueInc_Cleaned.csv',index=False)




















