
import pandas as pd
import numpy as np 


class BackTest():


	def __init__(self,test_data,strategy_func):

		self.strategy_specific_data = test_data["strategy_specific_data"]
		self.general_data = test_data["general_data"]
		self.strategy = strategy_func


	def __test_data_slicing(self,index,length):
		'''
		This function slices the test_data based on the index and the length
		of the sliced dataframe.

		:param index: indicates the end of the desired sub-dataframe
		:param length: the lenght of the sub-dataframe

		:return: sub-dataframe, the dataframe has the index [index-length,index]
		'''
		if index - length < 0:
			length = index

		storage = {}

		for key in self.strategy_specific_data.keys():
			data = self.strategy_specific_data[key]
			sub_data = data[index-length:index,:]
			storage[key] = sub_data

		return storage



	def __portfolio_return_calculation(self,weight,new_return):
		'''
		This function calculates the portfolio return in the next month based on this new weight.

		:param weight: np.array, the weight of each asset in the next month

		'''

		r_p = np.sum(weight * new_return)
		return r_p



	def historical_backtest(self,est_length,start_index,end_index,update=1,fixed=True):
		'''
		This function calculates the backtest performance on the historical data from start date to end_date.
		The strategy is estimated based on estimation data provided.

		'''	
		rp_storage = []
		weight_storage = []
		date_storage = []

		while start_index <= end_index:
			# slice the data get the estimation window and the next period return
			sub_data_dic = self.__test_data_slicing(start_index,est_length)

			# pass into the strategy function and calcualte the new weight
			func = self.strategy
			new_weight = func(sub_data_dic)
		

			# use the new weight to calculate the portfolio return
			new_return = self.general_data["ret_mat_test"][start_index,:]
			new_return = new_return.reshape(new_weight.shape[0],new_weight.shape[1])

			r_p = self.__portfolio_return_calculation(new_weight,new_return)
			
		#use start index date
			new_date = self.general_data['date'][start_index]

			rp_storage.append(r_p)
			weight_storage.append(new_weight)
			date_storage.append(new_date)

			start_index += update

		return rp_storage, weight_storage, date_storage
































