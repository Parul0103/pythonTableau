# -*- coding: utf-8 -*-
"""
Created on Thu May  4 00:19:56 2023

@author: Shikhar Mehra
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data 
json_file=open('loan_data_json.json')
data = json.load(json_file)

#method 2 to reqd json file 
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
 
#transform to data frame
loandata = pd.DataFrame(data)
initdata = loandata


#finding unique value from a column 
loandata['purpose'].unique()

#describe the data
loandata.describe()
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()
 

#using EXP() ->exponent to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


# fico=350
# if fico>=300 and fico<400:
#     ficocat='Very Poor'
# elif fico>=400 and fico<600:
#     ficocat='Poor'
# elif fico>=600 and fico<660:
#     ficocat='Fair'
# elif fico>=660 and fico<780:
#         ficocat='Good'
# elif fico>=780:
#     ficocat='Excellent'
# else:
#     ficocat='Unknown'
# print(ficocat)


print(loandata['fico'][0]) #displays 0th index value

ficocat=[]
print(len(loandata))#print no. of rows

for x in range(0,len(loandata)):
    category = loandata['fico'][x]
    #category = 'red'
    try:
        if category>=300 and category<400:
            cat='Very Poor'
        elif category>=400 and category<600:
            cat='Poor'
        elif category>=601 and category<660:
            cat='Fair'
        elif category>=660 and category<700:
            cat='Good'
        elif category>=700:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='errror'
   
    ficocat.append(cat)
#once cat value set it is added to ficocat

ficocat = pd.Series(ficocat)

loandata['fico.category']=ficocat

#df.loc as conditional statement
# df.loc[df[columname] condition, newcolumnname] = 'value if condtion is met'
# creates a new column according to condition 

#for interest rates a new column is wanted if  rate>0.12 then high then low
loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'high'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'low'


#number of loans/rows by fico.category
catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.9)
plt.show()

purposecount=loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='blue',width=0.9)
plt.show()

#scatterplot
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint,color='red')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)










































































































