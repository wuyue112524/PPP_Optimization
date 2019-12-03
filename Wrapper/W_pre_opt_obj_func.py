
import pandas as pd 
import numpy as np

from Wrapper.Moduel.M_WeightFunc import WeightFunction
from Wrapper.Moduel.M_UtilityFunc import UtilityFunction



def wrapper_objective_compo_creation(factor_dic,ticker_list,ret_mat,wb=None):
	
	T = ret_mat.shape[0]
	N = ret_mat.shape[1]

	storage = {}

	# create weight function
	if wb==None:
		wb = np.ones([T,N])/len(ticker_list)

	weight_creation = WeightFunction(factor_dic)
	weight_func = weight_creation.linear_weight_function(wb)

	storage["weight_function"] = weight_func

    # create return matrix
	storage["ret_matrix"] = ret_mat

    # create utility function
	utility_func_creator = UtilityFunction()
	util = utility_func_creator.crra_utility(risk_aversion=5)

	storage["utility_function"] = util

    # create portfolio return calculation function
	def portfolio_return_cal(theta,weight_func=weight_func,ret_mat=ret_mat):
		w_mat = weight_func(theta)
		wet_ret = w_mat * ret_mat
		rp = np.apply_along_axis(np.sum,1,wet_ret)
		return rp

	storage["rp_cal_func"] = portfolio_return_cal

	return storage



def wrapper_objective_func(param_dic):
	
	rp_cal_func = param_dic["rp_cal_func"]
	util = param_dic["utility_function"]


	def func(x):
		rp = rp_cal_func(x)
		util_vec = util(rp)
		ave_util = np.mean(util_vec)
		return -ave_util

	return func






















