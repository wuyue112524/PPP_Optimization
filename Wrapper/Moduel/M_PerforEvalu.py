
import pandas as pd
import numpy as np
import scipy.special
import scipy.optimize
from scipy.stats import norm
import scipy.stats as sta



class StrategyEvaluation():
    def __init__(self,ret_series,ret_date):
        self.performance = ret_series
        self.date = ret_date



    def cum_ret_calculation(self):

    	performance = self.performance + 1
    	cum_ret = performance.cumprod()
    	return cum_ret


    def drawdown_calculation(self):
    	cumret = self.cum_ret_calculation() - 1
    	cumret = np.array(cumret)
    	highwatermark = np.zeros(cumret.shape[0])
    	drawdown  = np.zeros(cumret.shape[0])
    	drawdownduration = np.zeros(len(cumret))

    	for t in range(1,cumret.shape[0]):
    		highwatermark[t] = np.maximum(highwatermark[t-1],cumret[t])
    		drawdown[t] = (cumret[t] + 1)/(highwatermark[t] + 1) - 1
    		if (drawdown[t]==0):
    			drawdownduration[t] = 0
    		else:
    			drawdownduration[t] = drawdownduration[t-1] + 1

    	return drawdown, np.min(drawdown), np.max(drawdownduration)


class ModelFreeEvaluation(StrategyEvaluation):
    
    def __init__(self,ret_series,ret_date):
        super().__init__(ret_series,ret_date)
        self.performance = self.performance.dropna()
    
    def sharpe_ratio(self,annul_freq,rf):

        excess_return = np.average(self.performance - rf)
        std = np.std(self.performance)
        annual_sharpe = annul_freq**0.5 * excess_return/std
        return annual_sharpe

    def excessive_downside_deviation(self,target=0):
        performance = self.performance
        excessive_return = performance - target
        excessive_return = excessive_return.dropna()
        negative_excessive_return = excessive_return[excessive_return <= 0]
        EDD = np.std(negative_excessive_return)
        return(EDD)



class ModelBasedEvaluation(StrategyEvaluation):


	def __init__(self,ret_series,ret_date):

		super().__init__(ret_series,ret_date)























