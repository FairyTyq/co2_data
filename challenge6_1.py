# -*- coding:utf-8 -*-
import pandas as pd
def co2(dataset):
    # ��ȡ������������仯���ݼ�
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheetname='Series')
    # 1.�鿴�����ļ��ṹ
    
    # 2.�����Һ����ڵ�����Ⱥ����������ϵ

    # 3.���� DataFrame �еĲ���Ҫ���ݺ�ȱʧ����
    # 4.ע��ȱʧֵ������NaN����ʽ
    # 5.�����շ��ص� DataFrame �������սҪ��ĸ�ʽ

    
    return results
