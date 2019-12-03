import pandas as pd
import numpy as np



class FactorsConstruction():
    '''
    Construct factors for different stocks
    '''

    def factor_scaler(self, dataframe,start_col,end_col):
        '''
        scale the factors so that cross-sectional mean = 0 and cross-sectional sd = 1
        
        :param dataframe (dataframe):
        :param start_col (int): start column we want to standardize
        :param end_col (int): end column we want to standardize


        :return (dataframe): a scaled factor dataframe
        '''
        dataframe = dataframe.iloc[:,start_col:end_col+1]
        mean = dataframe.apply(np.mean,1)
        std = dataframe.apply(np.std, 1)
        def func(x):
            stdarization = (x - mean) / std
            return stdarization

        factor_scaled = dataframe.apply(func,0)
        return factor_scaled




class ValueFactor(FactorsConstruction):




    def mktcap_calculation(self, price, shares_outstanding):
        '''
        Calculate stock market capitalization

        :param price (series):
        :param shares_outstanding (series):

        :return (series): market capitalization
        '''

        index_array = price.index == shares_outstanding.index
        if sum(index_array)==len(index_array):
            mktcap = price * shares_outstanding
        else:
            print("The dates don't match")


class QualityFactor(FactorsConstruction):
    pass




class TechnicalFactor(FactorsConstruction):
    


    def momentum_factor(self,series,frequency,look_back,skip=0,risk_adjust=False):
        '''
        This method is used to construct the momentum of the return series. The method also supports calculation of risk adjusted
        momemnt and skip that is used to avoid the short term reversal effect


        :param series:
        :param frequency:
        :param look_back:
        :param skip:
        :param risk_adjust:



        :return: series

        '''


        series = series.asfreq(frequency,"ffill")
    
        tot_length = len(series)
        factor_list = []
        ini_index = look_back
    
        while ini_index <= tot_length:
            
            sub_series = series[ini_index-look_back:ini_index]
            sub_series = sub_series+1
            cum_ret = sub_series.product()-1
            if risk_adjust:
                r_m = 0.02
                cum_ret = cum_ret-r_m
            
            factor_list.append(cum_ret)
            ini_index += 1
        
        index_list = list(series.index)
        ini_index = look_back-1+skip
        factor_index = index_list[ini_index:]
        
        factor_list = factor_list[0:len(factor_list)-skip]
        factor_list = pd.Series(factor_list)
        factor_list.index = factor_index
        
        return factor_list





  








