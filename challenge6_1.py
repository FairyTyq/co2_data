# -*- coding:utf-8 -*-
import pandas as pd
def co2(dataset):
    # 读取世界银行气候变化数据集
    df_climate = pd.read_excel(dataset,sheetname='Data')
    df_country = pd.read_excel(dataset,sheetname='Country')
    df_series = pd.read_excel(dataset,sheetname='Series')
    # 1.查看数据文件结构
    
    # 2.将国家和所在的收入群体类别产生联系
    df1_tmp = df_climate[['Country name','Series code',1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]]
    df1 = df1_tmp[df1_tmp['Series code']=='EN.ATM.CO2E.KT']
    df2 = df_country[['Country name','Income group']]
    # df_res = pd.concat([df2,df1],axis=1)
    df_res = df2.merge(df1)
    #df_res2 = df_res[df_res['Series code']=='EN.ATM.CO2E.KT']
    print(df_res.head(20))
    #df_merge = df_climate.merge(de_country,left_on='Country name',right_on='Country name',how='outer')
    # 3.处理 DataFrame 中的不必要数据和缺失数据
    # 4.注意缺失值并不是NaN的形式
    # 5.将最终返回的 DataFrame 处理成挑战要求的格式
    
    #return results

if __name__ == '__main__':
    co2('ClimateChange.xlsx')
