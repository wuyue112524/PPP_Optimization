import pandas as pd
import numpy as np
from Wrapper.Moduel.M_PanelFormatter import PanelDataManipulation, PanelDataReformat

class YFDataManipulation(PanelDataManipulation,PanelDataReformat):

    def __init__(self,df,ticker_list):

        self.df = df
        self.ticker_list = ticker_list
        self.panel_data = None


    def update_panel_data(self,panel_data):

        self.panel_data = panel_data
