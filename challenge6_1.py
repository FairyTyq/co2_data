# -*- coding:utf-8 -*-
import pandas as pd
def co2(dataset):
    # ��ȡ������������仯���ݼ�
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheetname='Series')
    # 1.�鿴�����ļ��ṹ
    
    # 2.�����Һ����ڵ�����Ⱥ����������ϵ
    df_merge = df_climate.merge(de_country,left_on='Country name',right_on='Country name',how='outer')
    # 3.���� DataFrame �еĲ���Ҫ���ݺ�ȱʧ����
    # 4.ע��ȱʧֵ������NaN����ʽ
    # 5.�����շ��ص� DataFrame �������սҪ��ĸ�ʽ
    de_merge['Country name','Income group',]
    
    return results
