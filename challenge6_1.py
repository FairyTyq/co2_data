# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

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
    # 将'..'替换成0，（还是说需要按照前面的数据进行填充？？）
    df_resa = df2.merge(df1).replace('..',np.nan)
    df_res = df_resa.fillna(method='ffill')
    df_res['sum']= df_res[[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]].apply(lambda x:x.sum(),axis=1)
    df_a = df_res[['Country name','Income group','Series code','sum']]
    print('df_a:%s'%df_a)
    df_b = df_a.groupby(['Income group'])
    df_c = pd.DataFrame({'Sum emissions':df_b['sum'].sum(),'Highest emissions':df_b['sum'].max(),'Lowest emissions':df_b['sum'].min()})
    print('df_c%s'%df_c)
    #print('test print: %s'%df_b['sum'].min()['High income: OECD'])
    ted = df_b['sum'].min()['High income: OECD']
    print(df_a[df_a['sum']==ted]['Country name'])
    
    #print('loc%s'%df_c.loc[])
    # 3.处理 DataFrame 中的不必要数据和缺失数据
    # 4.注意缺失值并不是NaN的形式
    # 5.将最终返回的 DataFrame 处理成挑战要求的格式
    
    #return results

if __name__ == '__main__':
    co2('ClimateChange.xlsx')
