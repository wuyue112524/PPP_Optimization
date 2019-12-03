import pandas as pd 
from Wrapper.Moduel.M_DataMani import BasicManipulation

class PanelDataManipulation(BasicManipulation):

	def __init__(self,df,ticker_list):
		self.df = df
		self.ticker_list = ticker_list


	def panel_data_construction(self,colname_list,frequency="B",na_action="forward"):
		storage_df = []
		for ticker in self.ticker_list:
			sub_df = self.df[ticker]
			storage_series = []
			for col in colname_list:
				series = sub_df[col]
				if pd.isnull(series[-1]):
					print(ticker + " has been delisted during the period.")
				series = self.missing_value_manipulation(series,method=na_action,frequency=frequency,business=True)
				storage_series.append(series)
			sub_df = pd.concat(storage_series,axis=1)
			sub_df["ticker"] = ticker
			storage_df.append(sub_df)
		final = pd.concat(storage_df)
		return final









class PanelDataReformat():



	def __init__(self,panel_data,ticker_list):

		self.panel_data = panel_data
		self.ticker_list = ticker_list




	def panel_data_sort_reindex(self,sort_list,index_name):

		self.panel_data = self.panel_data.sort_values(by=sort_list)
		self.panel_data.index = self.panel_data[index_name]
		print("Done Sorting and Indexing")




	def panel_data_apply(self,func,ticker_list=None):
		if ticker_list== None:
			ticker_list = self.ticker_list

		storage = []
		for ticker in ticker_list:
			sub_df = self.panel_data[self.panel_data.ticker==ticker]
			sub_df = func(sub_df)
			storage.append(sub_df)
		df = pd.concat(storage)
		return df



	def panel_data_refreq(self,freq,method="ffill"):
		
		def func(x):
			return pd.DataFrame.asfreq(x,freq,method)

		result = self.panel_data_apply(func)
		return result



	def panel_data_shift(self,target_name,shift_step=-1):
		
		def func(x,shift_step=shift_step,shift_target=target_name):
			x[shift_target] = x[shift_target].shift(shift_step)
			return x

		result = self.panel_data_apply(func)

		return result


	def display_effective_obs(self,ticker_list=None):
		if ticker_list == None:
			ticker_list =self.ticker_list
		def func(x):
			x = x.dropna()
			if x.shape[0] == 0:
				no_eff_obs = [0]
				min_date = [pd.to_datetime('1800-01-01',format='%Y-%m-%d')]
				max_date = [pd.to_datetime('1800-01-01',format='%Y-%m-%d')]
				
			else:	
				no_eff_obs = [x.shape[0]]
				min_date = [min(x.date)]
				max_date = [max(x.date)]
				
			sub_df = pd.DataFrame({"no_eff_obs":no_eff_obs,"min_date":min_date,"max_date":max_date})
			return sub_df

		df = self.panel_data_apply(func,ticker_list)
		df['ticker'] = ticker_list
		return df















