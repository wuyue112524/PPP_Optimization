import pandas as pd
import numpy as np



def portfolio_return_calculation(r_mat,w_mat):
    
    weighted_ret = r_mat * w_mat
    r_p = np.apply_along_axis(np.sum,1,weighted_ret)
    return r_p




def single_factor_reshape(factor_series,number_of_assets,number_of_dates):
    '''
    factor_series:1. the date for each factor should match each other
                  2. main sort by stock, then sort by date
    N: number of assets
    T: number of dates for each asset
    '''
    factor_array = np.array(factor_series)
    results = factor_array.reshape(number_of_assets,number_of_dates).T
    return results





def factor_data_reshape(factor_colname_list,dataframe,number_of_assets,number_of_dates):
    
    storage_dic = {}
    
    for factor in factor_colname_list:
        
        series = dataframe[factor]
        reshape_df = single_factor_reshape(factor_series = series,
                                           number_of_assets = number_of_assets,
                                           number_of_dates = number_of_dates)
        
        storage_dic[factor] = reshape_df
        
    return storage_dic



    return result

def weight_prediction(wb,theta,factor):
    '''
    :pars:wb(arrary) N X 1
    :pars:theta(array) K X1
    :pars:factor(array) K X N
    '''
    N = wb.shape[0]
    active_weight = np.matmul(factor.T,theta)/N
    final_weight = wb + active_weight
    return final_weight

def get_new_factor_value(factor_dic,factor_list,new_factor_row=-1):
    
    new_factor_list = []
    
    for factor in factor_list:
        single_factor_df = factor_dic[factor]
        new_single_factor = single_factor_df[new_factor_row,:]
        new_factor_list.append(new_single_factor)
    
    new_factor_list = np.array(new_factor_list)
    
    return new_factor_list