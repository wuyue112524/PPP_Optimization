import pandas as pd
import numpy as np

class UtilityFunction():
    '''Contains different utility functions'''

    def hara_utility():
        pass

    def crra_utility(self,risk_aversion=5,derivative=False):



        if derivative:

            def func(rp):

                if risk_aversion == 1:
                    result = 1/rp
                else:
                    result = (1+rp)**(-risk_aversion)
                return result
        else:
            def func(rp):
                rp = rp[~np.isnan(rp)]
                if risk_aversion == 1:
                    utility = np.log(rp)
                else:
                    utility = (1 + rp) ** (1 - risk_aversion) / (1 - risk_aversion)

                return utility

        return func

    def exponential_utility(self, portfolio_return, risk_aversion):
        pass