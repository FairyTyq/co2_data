# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

def co2():
    # 读取世界银行气候变化数据集
    dataset = 'ClimateChange.xlsx'
    df_climate = pd.read_excel(dataset,sheetname='Data')
    df_country = pd.read_excel(dataset,sheetname='Country')
    df_series = pd.read_excel(dataset,sheetname='Series')
    # 1.查看数据文件结构
    
    # 2.将国家和所在的收入群体类别产生联系
    df_st = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    #df1_tmp = df_climate[['Country name','Series code',1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]]
    df1_tmp = df_st[[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]]
    df1_tmp1 = df1_tmp.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df1_tmp1['Country name'] = df_st['Country name']
    df1_tmp1['Series code'] = df_st['Series code']
    df1 = df1_tmp1.dropna(axis=0,how='all').dropna(axis=1,how='all')
    
    #df1 = df1_tmp[df1_tmp['Series code']=='EN.ATM.CO2E.KT']
    df2 = df_country[['Country name','Income group']]
    # 将'..'替换成0，（还是说需要按照前面的数据进行填充？？）
    df_res = df2.merge(df1).replace('..',np.nan)
    #df_resb = df_resa.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    #df_res = df_resb.dropna(axis=0,how='all')
    print(df_res.head(10))
    df_res['total']= df_res[[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]].apply(lambda x:x.sum(),axis=1)
    df_a = df_res[['Country name','Income group','Series code','total']]
    df_b = df_a.groupby(['Income group'])
    
    # 获取各个收入群体内最低排放的国家名字
    
    df_low = df_b.apply(lambda t:t[t.total==t.total.min()])
    Low_ess = df_low['Country name']
    
    # 获取相应收入群体里排放量最高的国家名称
    
    df_high = df_b.apply(lambda t:t[t.total==t.total.max()])
    High_ess = df_high['Country name']
    
    index_tmp = ['High income: OECD','High income: nonOECD','Low income','Lower middle income','Upper middle income']
    columns_tmp = ['Income group','Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results = pd.DataFrame(list(zip(index_tmp,df_b['total'].sum(),High_ess,df_high['total'],Low_ess,df_low['total'])),columns=columns_tmp).set_index('Income group')
    print(results)
    
    
    #print('loc%s'%df_c.loc[])
    # 3.处理 DataFrame 中的不必要数据和缺失数据
    # 4.注意缺失值并不是NaN的形式
    # 5.将最终返回的 DataFrame 处理成挑战要求的格式
    return results

if __name__ == '__main__':
    co2()
