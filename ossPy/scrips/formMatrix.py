#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:55:10 2020

@author: dnb3k
"""
import scipy

substringMatrix=scipy.sparse.coo_matrix((len(tableUniqueFullNameCounts.index),len(tableUniqueFullNameCounts.index)),dtype=bool)

accessibleMatrix=substringMatrix.tolil()

#iterate acroos unique listings
for index, row in tableUniqueFullNameCounts.iterrows():
    
    #formulate a good regex expression
    currentRegex=re.compile('(?i)\\b'+re.escape(tableUniqueFullNameCounts['company'].loc[index])+'\\b')
    
    #get all company listings that feature the current company string
    currentBool=tableUniqueFullNameCounts['company'].str.contains(currentRegex)
    
    accessibleMatrix[index,:]=currentBool