import pandas as pd 
import numpy as np
from Wrapper.W_momen_factor_create import *
from Wrapper.W_pre_factor_data_mani import *
from Wrapper.W_pre_opt_data_mani import wrapper_df_preparation
from Wrapper.W_pre_opt_obj_func import (wrapper_objective_compo_creation,
                                             wrapper_objective_func)
import scipy.optimize as opt
from Wrapper.Moduel.M_FactorCreator import FactorsConstruction
from Wrapper.W_pre_opt_factor_standardize import wrapper_standardize_factor
from Wrapper.Moduel.M_SupportFunction import (weight_prediction,get_new_factor_value)



def PPP_optimize(data_dict,ticker_list,factor_list, initial_guess=None):
    '''
    
    :param:data_dic dictionary of dictionary  
    '''
    #get data from data_dic 
    
    strategy_specific_data = data_dict
    ret_mat = strategy_specific_data['ret_mat']
    
    # will alter the strategy_specific_data dictionary 
    # and need to rerun to get correct value each time 
    del strategy_specific_data['ret_mat']
    factor_dic = strategy_specific_data
   
    
    param_dic = wrapper_objective_compo_creation(factor_dic,ticker_list,ret_mat)
    objective_func = wrapper_objective_func(param_dic=param_dic)
    if initial_guess == None:
        x0 = [1.0]*len(factor_dic)    
    myoptions = {"disp":True}
    opt_results = opt.minimize(objective_func,x0,options=myoptions,method = 'Nelder-Mead')
    N= len(ticker_list)
    theta = opt_results['x']
    theta = np.reshape(theta,[theta.shape[0],1])
    wb = np.ones((N,1))/N
    factor = get_new_factor_value(factor_dic,factor_list,new_factor_row=-1)
    final_weight = weight_prediction(wb,theta,factor)
    return final_weight.T