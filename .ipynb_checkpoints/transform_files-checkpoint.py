#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

# def drop_irrelevant_cols(df):
#     df.drop(['Dystopia.Residual', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual','Whisker.low','Whisker.high'], axis=1, inplace=True)
#     return df

def rename_cols(df):
    df.rename(columns={'Country or region': 'Country', 'Happiness.Score' : 'Happiness Score','Score':'Happiness Score', 'Economy..GDP.per.Capita.':'GDP per capita','Economy (GDP per Capita)':'GDP per capita',
                        'Freedom to make life choices':'Freedom','Trust (Government Corruption)':'Perceptions of corruption','Trust..Government.Corruption.':'Perceptions of corruption',
                        'Health (Life Expectancy)':'Healthy life expectancy','Health..Life.Expectancy.':'Healthy life expectancy'}, inplace=True)
    return df

def reorder_cols(df):
    csv_file = df.reindex(columns=['Year','Country','Happiness Score','GDP per capita','Social support','Healthy life expectancy','Freedom','Generosity','Family','Perceptions of corruption'])
    return csv_file

def replace_empty_value(df):
    df['Social support'] = df['Social support'].fillna(0)
    df['Family'] = df['Family'].fillna(0)
    return df

def float_to_int(df):
    df['region-code'] = df['region-code'].fillna(0)
    df['sub-region-code'] = df['sub-region-code'].fillna(0)
    df['intermediate-region-code'] = df['intermediate-region-code'].fillna(0)
    df['country-code'] = df['country-code'].fillna(0)
    df = df.astype({"country-code":"int","region-code":"int","sub-region-code":"int","intermediate-region-code":"int"})
    return df

def status_calc(df_happiness):
    conditions = [
    (df_happiness['Happiness Score'] > 5.6),
    (df_happiness['Happiness Score'] >= 2.6) & (df_happiness['Happiness Score'] <= 5.6),
    (df_happiness['Happiness Score'] < 2.6)
    ]
    values = ['Green', 'Amber', 'Red']
    happ_values = np.select(conditions, values)
    return happ_values


# In[ ]:




