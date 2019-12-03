
import pandas as pd
import numpy as np


class BasicManipulation:
    def __init__(self):
        self.df = None
        self.panel_data = None
        self.ticker_list = None

    def single_series_return_calculation(self,series,log_ret=True,frequency='D'):
        """This calculates the required return of a single series of corresponding frequency.
        The default frequency is daily, and the method will forward filling the missing values

        :param series: pd.Series, the series should be indexed by the date
        :param: log_ret: boolean, indicate whether to use log return
        :return: pd.Series
        """

        price_after_freq = series.asfreq(frequency,method='ffill')
        series = price_after_freq

        if log_ret==True:
            series_t=np.log(series)
            series_t_n = series_t.shift(1)
            ret_series = series_t - series_t_n
        else:
            ret_series=(series-series.shift(1))/series.shift(1)


        return ret_series

    def multiple_asset_return_calculation(self,dataframe,by,target,index_name,ticker_list,frequency='D',log_ret = True):
        """
        This methods calculates the required return of multiple single assets stored in a dataframe based on corresponding frequency

        :param by: str
        :param: target: str
        :param index_name: str
        :param ticker_list: list(str)
        :return: Dataframe, with three columns
        """
        dataframe[index_name] = pd.to_datetime(dataframe[index_name])
        storage = []
        
        for ticker in ticker_list:
            ## get a sub dataframe and get series
            sub_df = dataframe[dataframe[by]==ticker]
            sub_df.index = sub_df[index_name]
            series = sub_df[target]
            series = series.sort_index()
        ## pass into the function get the return series
            series_ret = self.single_series_return_calculation(series,log_ret,frequency)

        ## convert to dataframe and add ticker column
            series_ret = pd.DataFrame(series_ret)
            series_ret[by] = ticker
            series_ret[index_name] = series_ret.index

        ## save to the storage
            storage.append(series_ret)


        # convert storage into dataframe 
        results = pd.concat(storage,ignore_index=True)
        cols = [by,index_name,target]
        results = results[cols]
        return results


    def missing_value_manipulation(self,series,method="forward",frequency="B",business=True):
        """
        This methods cleans the missing value within a single series.
        
        :param method: str, it indicates the method to use for missing value cleaning
        :param series: pd.Series, index

        :nreturn: it updates the series directly
        """

        if business:
            start_date = series.index[0]
            end_date = series.index[-1]
            new_date_index = pd.date_range(start_date,end_date,freq=frequency)
            new_series = series.reindex(new_date_index)
        else:
            new_series = series

        if method == "drop":
            new_series = new_series.dropna()
        elif method == "forward":
            new_series = new_series.fillna(method="ffill")
        elif method == "backward":
            new_series = new_series.fillna(method="bfill")
        else:
            print("Undefined Method")

        return new_series



    def dataframe_slicing(self,start_date,end_date):
        '''
        This method slices the given dataframe that are within the given period.

        :param df: dataframe, the index has to be date
        :param start_date: datetime, it has to have the format %Y-%m-%d
        :param end_date: datetime, it has to have the format %Y-%m-%d

        :return: dataframe
        '''
        df = self.df
        
        start_date = pd.to_datetime(start_date,format="%Y-%m-%d")
        end_date = pd.to_datetime(end_date,format="%Y-%m-%d")
        df_index = list(df.index)

        indicator = [(date>=start_date) & (date<=end_date) for date in df_index]

        if len(indicator) == 0:
            print("There is no date matching the target period.")
            pass

        sub_df = df[indicator]

        return sub_df
























































