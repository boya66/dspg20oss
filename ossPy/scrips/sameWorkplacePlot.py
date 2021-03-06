#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:16:24 2020
This function creates a plot that depicts the number of people that work at
a company that has some number of employees associated with it.  

@author: dnb3k
"""
import ossPyFuncs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#form and perform the query
postgreSql_selectQuery="SELECT login, company FROM gh.ctrs_raw ;"
result=ossPyFuncs.queryToPDTable(postgreSql_selectQuery)

#obtain the eralse list
currentDir=os.path.dirname('ossPyFuncs.py')
eraseList=pd.read_csv(os.path.join(currentDir,'keyFiles/eraseStrings_v6.csv'),quotechar="'",header=None)
#apply the erase list
semiCleanedOutput=pd.DataFrame(ossPyFuncs.eraseFromColumn(eraseList['company'],eraseList))
#apply a lower to increase convergence/overlap
lowerInput=pd.DataFrame(semiCleanedOutput['company'].str.lower())

#get the unique counts
companyCounts=lowerInput['company'].value_counts()

#establish the binvals
binVals=np.asarray([0,1,5,10,20,50,100,200,np.max(companyCounts)])

#iterate to sum the number of employees meeting the criterion
binSum=np.zeros([len(binVals)-1,1])
for iBins in range(len(binVals)-1):
    binSum[iBins]=sum(companyCounts[np.logical_and(companyCounts>binVals[iBins],companyCounts<=binVals[iBins+1])])

#import plotting package
import seaborn as sns
#set the name vector    
binNames=['1 ','2-5 ','6-10 ','11-20 ','21-50 ','51-100 ','101-200 ', '>201']
#set the axes labels
workplaceSizeTable=pd.DataFrame(columns=["same workplace","Number of Persons"])
workplaceSizeTable['Number of Persons']=np.squeeze(binSum)
workplaceSizeTable['same workplace']=np.squeeze(binNames)

#plot the output
sns.catplot(data=workplaceSizeTable, kind="bar", x='same workplace',y='Number of Persons', palette='Spectral');
plt.figure(figsize=(16,32),dpi=200)