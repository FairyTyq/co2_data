# -*- coding:utf-8 -*-
import pandas as pd

def co2():
    # 读取世界银行气候变化数据集
    dataset = 'ClimateChange.xlsx'
    df_climate = pd.read_excel(dataset,sheetname='Data')
    df_country = pd.read_excel(dataset,sheetname='Country')
    df_series = pd.read_excel(dataset,sheetname='Series')
    # 1.查看数据文件结构
    
    # 2.将国家和所在的收入群体类别产生联系
    df_st = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df1 = df_st[['Country code',1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]].set_index('Country code')
    df1.replace({'..':pd.np.NaN},inplace=True)
    df1 = df1.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df1.dropna(how='all',inplace=True)
    df1['total'] = df1.sum(axis=1)

    
    df2 = df_country[['Country code','Country name','Income group']].set_index('Country code')
    
    df_comb = pd.merge(df1,df2,left_index=True,right_index=True)
    df_groupby = df_comb.groupby('Income group')
    
    # 获取各个收入群体内最低排放的国家名字
    
    df_low = df_groupby.apply(lambda t:t[t.total==t.total.min()])
    Low_ess = df_low['Country name']
    
    # 获取相应收入群体里排放量最高的国家名称
    
    df_high = df_groupby.apply(lambda t:t[t.total==t.total.max()])
    High_ess = df_high['Country name']
    
    index_tmp = ['High income: OECD','High income: nonOECD','Low income','Lower middle income','Upper middle income']
    columns_tmp = ['Income group','Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results = pd.DataFrame(list(zip(index_tmp,df_groupby['total'].sum(),High_ess,df_high['total'],Low_ess,df_low['total'])),columns=columns_tmp).set_index('Income group')
    print(results)
    
    
    #print('loc%s'%df_c.loc[])
    # 3.处理 DataFrame 中的不必要数据和缺失数据
    # 4.注意缺失值并不是NaN的形式
    # 5.将最终返回的 DataFrame 处理成挑战要求的格式
    return results

if __name__ == '__main__':
    co2()
