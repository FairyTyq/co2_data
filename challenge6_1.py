# -*- coding:utf-8 -*-
import pandas as pd
def co2(dataset):
    # 读取世界银行气候变化数据集
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheetname='Series')
    # 1.查看数据文件结构
    
    # 2.将国家和所在的收入群体类别产生联系
    df_merge = df_climate.merge(de_country,left_on='Country name',right_on='Country name',how='outer')
    # 3.处理 DataFrame 中的不必要数据和缺失数据
    # 4.注意缺失值并不是NaN的形式
    # 5.将最终返回的 DataFrame 处理成挑战要求的格式
    de_merge['Country name','Income group',]
    
    return results
