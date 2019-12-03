import pandas as pd
from Wrapper.Moduel.M_FactorCreator import FactorsConstruction
import numpy as np

def wrapper_standardize_factor(ticker_list,factor_dic):
    storage = {}
    for key in factor_dic.keys():
        factor = factor_dic[key]
        factor = pd.DataFrame(factor)
        sample_obj = FactorsConstruction()
        N = len(ticker_list)
        sta_factor = sample_obj.factor_scaler(factor, start_col=0, end_col= N)
        sta_factor = np.array(sta_factor)
        storage[key] = sta_factor
    return storage