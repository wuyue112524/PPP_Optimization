import numpy as np
import pandas as pd


class WeightFunction:
    def __init__(self,factor_dic):
        self.factor_dic = factor_dic

    def linear_weight_function(self,wb):
        '''
        each factor should have the same length
        construct linear weight function which is the following:
        w = wb + 1/N (theta_1 * factor_1 +theta_2 * factor_2 +... +theta_n *factor_n)
        factor_dic(dictionary): keys:factor name, values: factor values
        wb 
        '''
        n_factor = len(self.factor_dic)
        key_list = list(self.factor_dic.keys())
        key_list.sort()
        T = self.factor_dic[key_list[0]].shape[0]
        N = self.factor_dic[key_list[0]].shape[1]
        
        def func(theta):
            summation = np.zeros([T,N])
            for i in range(0,n_factor):
                factor = self.factor_dic[key_list[i]]
                summation = summation + factor*theta[i]
            
            w = summation/N + wb
            return w
        return func

























