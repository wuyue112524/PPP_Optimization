import pandas as pd
import numpy as np
import os
from Wrapper.Moduel.M_FactorCreator import TechnicalFactor

class FacControl():



    def bulk_moment_factor_creation(self,sub_df,frequency,look_back_list,skip=0,target_name='price'):
        '''
        :pars:sub_df 
        :pars:target_name:price 
        :pars:frequency
        :look_back_list: a list should be increasing
        :skip: skip window
    
        return a factor dataframe
        
            '''
        factor_creator = TechnicalFactor()
        
        storage = {}
        
        for look_back in look_back_list:
            series = sub_df.price
            series.index = sub_df["date"]
            factor = factor_creator.momentum_factor(series,frequency,
                                                    look_back=look_back,
                                                    skip=0,
                                                    risk_adjust= False)
            name = "momentum" + "_" + str(look_back)
            storage[name] = factor
    
    
        basis = storage["momentum" + "_" + str(look_back_list[0])]
        basis = pd.DataFrame(basis)
    
        for index in range(1,len(look_back_list)):
            
            incremental_df = storage["momentum" + "_" + str(look_back_list[index])]
            incremental_df = pd.DataFrame(incremental_df)
            basis = basis.merge(incremental_df,how="left",left_index = True,right_index = True)
        
        name_list = ["momentum" + "_" + str(look_back) for look_back in look_back_list]
        basis.columns = name_list
    
        return basis
    

    def momentum_factor_creation(self,return_df,ticker_list,frequency,look_back_list,skip=0,target_name='price'):
        '''
        :pars: return_df(pd.dataframe)
        :pars: ticker_list(list)
        :pars: frequency:(str) ex:'BM'
        :pars:look_back_list(list): the look back window list to create momentum factors
        :pars:skip(int)
        :pars:target_name(str): the name of return column 
        '''
        storage=[]
        for ticker in ticker_list:
            sub_df = return_df[return_df['ticker']==ticker]
            sub_df.index = sub_df.date
            sub_df = self.bulk_moment_factor_creation(sub_df,frequency,look_back_list,skip=0,target_name='price')
            sub_df['ticker'] =ticker
            storage.append(sub_df)
        factor_df = pd.concat(storage)
    
        factor_df['date'] = factor_df.index
        name = list(factor_df.columns)
        momentum_names = name[0:-2]
        new_name = ['date','ticker']+momentum_names
        factor_df = factor_df[new_name]
    
        return factor_df    


