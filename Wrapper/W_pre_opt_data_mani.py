
import Wrapper.Moduel.M_SupportFunction as sf
from Wrapper.Moduel.M_PanelFormatter import PanelDataReformat
from Wrapper.Moduel.M_FactorCreator import FactorsConstruction




def wrapper_df_preparation(ret_data,factor_data,factor_list):
	'''
	This function inputs two dataframe
	1. return dataframe, three columns
	2. factor dataframe, multiple factors with date and ticker column
	Factor list: the number of factors you want to fit into the final PPP model.
	It will retrun a dictionary that contains all factors in a NT matrix format
	It will also return a return matrix that is shift one observation ahead.



	'''

	ticker_list = list(set(ret_data.ticker))
	ticker_list.sort()

	N = len(ticker_list)
	T = len(factor_data[factor_data.ticker==ticker_list[0]].date)

	factor_dic = sf.factor_data_reshape(factor_colname_list=factor_list
		,dataframe=factor_data
		,number_of_assets=N
		,number_of_dates=T)



	panel_data_formatter = PanelDataReformat(ret_data,ticker_list)

	ret_forward_1_df = panel_data_formatter.panel_data_shift(target_name="price",shift_step=-1)
	ret_forward_1_df = ret_forward_1_df.sort_values(by=["ticker","date"])
	ret_mat = sf.single_factor_reshape(factor_series = ret_forward_1_df.price,
		number_of_assets = N,
		number_of_dates = T)


	return {"factor_dic":factor_dic,"ret_mat":ret_mat}




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










