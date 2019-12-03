import pandas as pd
import numpy as np
from Wrapper.Moduel.M_BackTest import BackTest
from Wrapper.Moduel.M_DataMani import BasicManipulation

class BenchmarkStrategy():
	def __init__ (self,ret_series,ret_date):
		'''
		:param:ret_series: return series of proposed strategy
		:param:ret_date: return date of proposed date  

		'''
		self.ret_series = ret_series
		self.ret_date = ret_date

		

	def __strategy_ret_calculation(self,strategy_func,data,est_length,update=1,fixed=True):
		
		start_date = self.ret_date[0]
		end_date = self.ret_date [-1]
		date_list = data['general_data']['date']
		
		start_index = date_list[date_list==start_date].index[0]
		end_index = date_list[date_list==end_date].index[0]

		obj = BackTest(data,strategy_func)

		rp_storage, weight_storage, date_storage = obj.historical_backtest(est_length,start_index,end_index,update=1,fixed=True) 

		return_dict = {'benchmark_return':rp_storage,'date':date_storage}

		final_return_df = pd.DataFrame(return_dict) 

		return final_return_df

	def equalweight(self,data,asset_num, update=1,fixed=True):
		'''
		:param: data: data dictionary
		:param: est_length: window length
		
		return: three array
		'''
		
		
		def strategy_func(x): 
		
			return np.ones([1, asset_num])/asset_num 

		#call the strategy_ret_calculation

		final_return_df = self.__strategy_ret_calculation(strategy_func = strategy_func,
																data=data,est_length=10,update=1,fixed=True)

		final_return_df['strategy_return'] =self.ret_series

		return final_return_df








class BenchmarkIndex():

	def __init__(self,ret_series,ret_date):

		self.ret_series = ret_series
		self.ret_date = ret_date


	def __benchmark_import(self,address):

		df = pd.read_csv(address)
		df.date = pd.to_datetime(df.date,format="%Y%m%d")
		return df



	def __data_matching(self,index_series,ret):

		index_df = pd.DataFrame(index_series)
		date = pd.DataFrame(self.ret_date)
		merge_df = date.merge(index_df,how="outer",left_on="date",right_index=True)
		merge_df = merge_df.sort_values("date")
		merge_df = merge_df.fillna(method="ffill")

		indicator = [day in list(self.ret_date) for day in merge_df.date]
		merge_df = merge_df[indicator]
		return merge_df





	def sp500_index_comparison(self,ret=True):

		index_df = self.__benchmark_import("Data/Index_sp500.csv")
		index_series = index_df["sp500"]
		index_series.index = index_df["date"]

		index_df = self.__data_matching(index_series,ret)
		if ret:
			series = index_df["sp500"]
			series.index = index_df["date"]
			ret_series=(series-series.shift(1))/series.shift(1)
			index_df["sp500"] = list(ret_series)

		index_df["strategy"] = self.ret_series
		return(index_df)



































