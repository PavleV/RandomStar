#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:08:16 2023

@author: a007678
"""



def randomStar(myList):
    
    """
    The randomStar function takes a pandas dataframe with one column and 
    returns a dataframe with an additional column that is like the original but
    shifted by one.
    
    """
    
    myList["R1"] = myList[0]
    last_element = myList['R1'].iloc[-1]
    myList['R1'].iloc[1:] = myList['R1'].iloc[:-1]
    myList['R1'].iloc[0] = last_element
    
    print(myList)
    
    
    
    
if __name__ == "__main__":
    
    import pandas as pd

    classList = pd.read_csv("ClassList.csv", header = None)
    
    classList2 = classList.sample(frac=1).reset_index(drop=True)
    
    classList3 = pd.concat([classList,classList2], ignore_index=True)
    
    randomStar(classList3)

