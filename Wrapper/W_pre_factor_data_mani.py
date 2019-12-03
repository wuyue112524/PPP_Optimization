#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import os
from Wrapper.Moduel.M_DataMani import BasicManipulation
from Wrapper.Moduel.M_FactorCreator import TechnicalFactor
from Wrapper.Moduel.M_FactorController import FacControl


def wrapper_import_data(price_file):
    ''':pars:price_file(str): the name of price data
       
        return: a price dataframe and a factor dataframe
        
        Note:The format for the price dataframe:{ticker}|{date}|{price}
    '''
    price_df = pd.read_csv(price_file)
    price_df['date']=pd.to_datetime(price_df['date'],yearfirst=True)
    ticker_list=list(set(price_df['ticker']))
    ticker_list.sort()
    return price_df,ticker_list

#return_df,ticker_list,frequency,look_back_list,skip=0,target_name='price'




def wrapper_factor_return_output(return_df,factor_df):
    #drop navalue
    factor_df = factor_df.dropna()

    #merge return data
    merged_df = factor_df.merge(return_df,how='left',on=['ticker','date'])
    
    factor_df = merged_df.iloc[:,:-1]
    return_df = merged_df.iloc[:,[0,1,-1]]
    
    
    return factor_df, return_df 



