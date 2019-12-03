import yfinance as yf
import pandas as pd
import os

class GetStockData():
    def __init__(self,ticker_list):
        self.ticker_list = ticker_list
    
    def __ticker_tostr__(self):
        '''
        convert ticker_list to a long string
        '''
        stop= ' '
        ticker_str = stop.join(self.ticker_list)
        return ticker_str
    
    def download_price(self,period='max',interval ='1d'):
        ticker_str = self.__ticker_tostr__()
        df = yf.download(self.ticker_list,period =period,interval=interval,group_by='ticker')
        return df
    
    def download_stock_info(self):
        pass
    
    def download_accounting(self):
        pass
    
    def download_balance_sheet(self):
        pass
    
    def download_cash_flow(self):
        pass
    
    def download_earnings(self):
        pass