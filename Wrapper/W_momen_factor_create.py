from Wrapper.Moduel.M_DataMani import BasicManipulation
from Wrapper.Moduel.M_FactorController import FacControl


def wrapper_return_calculation(price_df, ticker_list,look_back_list,skip=0,target_name='price',frequency='BM'):
    '''
    :pars:price_df
    :pars:ticker_list
    :pars:look_back
    '''
    ret_manipulation_obj = BasicManipulation()
    return_df =ret_manipulation_obj.multiple_asset_return_calculation(price_df,by='ticker',target='price',index_name='date',ticker_list=ticker_list,frequency =frequency,log_ret=False)
    factor_obj = FacControl()
    factor_df = factor_obj.momentum_factor_creation(return_df=return_df,
    												ticker_list=ticker_list,
    												frequency=frequency,
    												look_back_list=look_back_list,
    												skip=skip,
    												target_name=target_name)

    

    return return_df, factor_df
