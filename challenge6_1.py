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
    df_res['total']= df_res[[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]].apply(lambda x:x.sum(),axis=1)
    df_a = df_res[['Country name','Income group','Series code','total']]
    df_b = df_a.groupby(['Income group'])
    
    # 获取各个收入群体内最低排放的国家名字
#    hio = df_b['sum'].min()['High income: OECD']
#    c_hio = pd.Series(df_a[df_a['sum']==hio]['Country name'])
#    
#    hino = df_b['sum'].min()['High income: nonOECD']
#    c_hino = pd.Series(df_a[df_a['sum']==hino]['Country name'])
#    
#    li = df_b['sum'].min()['Low income']
#    c_li = pd.Series(df_a[df_a['sum']==li]['Country name'])
#    
#    lmi = df_b['sum'].min()['Lower middle income']
#    c_lmi = pd.Series(df_a[df_a['sum']==lmi]['Country name'])
#    
#    umi = df_b['sum'].min()['Upper middle income']
#    c_umi = pd.Series(df_a[df_a['sum']==umi]['Country name'])
    
    df_low = df_b.apply(lambda t:t[t.total==t.total.min()])
    # 转化为list
    Low_ess = df_low['Country name']
    
    # 获取相应收入群体里排放量最高的国家名称
#    l_hio = df_b['sum'].max()['High income: OECD']
#    c_l_hio = pd.Series(df_a[df_a['sum']==l_hio]['Country name'])
#    
#    l_hino = df_b['sum'].max()['High income: nonOECD']
#    c_l_hino = pd.Series(list(pd.Series(df_a[df_a['sum']==l_hino]['Country name']))[0])
#    
#    l_li = df_b['sum'].max()['Low income']
#    c_l_li = pd.Series(df_a[df_a['sum']==l_li]['Country name'])
#    
#    l_lmi = df_b['sum'].max()['Lower middle income']
#    c_l_lmi = pd.Series(df_a[df_a['sum']==l_lmi]['Country name'])
#    
#    l_umi = df_b['sum'].max()['Upper middle income']
#    c_l_umi = pd.Series(df_a[df_a['sum']==l_umi]['Country name'])
    
    df_high = df_b.apply(lambda t:t[t.total==t.total.max()])

    # 转化为list
    High_ess = df_high['Country name']
    #print("LOW ESS :  %s"%Low_ess)
    #print("HIGH ESS :  %s"%High_ess)
    #print('df_b%s'%df_b['total'].max())
    #print('df_high%s'%df_high)
    #results = pd.DataFrame({'Sum emissions':df_b['total'].sum(),"Highest emission country":High_ess,'Highest emissions':df_high['total'],"Lowest emission country":Low_ess,'Lowest emissions':df_low['total']})
    
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
    co2('ClimateChange.xlsx')
