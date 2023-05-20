# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 21:35:39 2022

@author: umave
"""
# import os
import pandas as pd
import numpy as np
import plotly.express as px


# selecting specific data
fuel_types = [
    'Regular Unleaded Gasoline',
    'Diesel',
    'Compressed Natural Gas',
    'Mid-Grade Gasoline',
    'Premium Gasoline',
    'Auto Propane'
]


if __name__ == '__main__':
    # importing data
    file = r'.\data\weekly_fueltypesall.csv'
    df_fuel_weekly = pd.read_csv(file)

    analysis_data = ['Date', 'Fuel Type']
    cities = ['Toronto West/Ouest', ]
    analysis_data.extend(cities)
    df = df_fuel_weekly[analysis_data]

    # breaking down data into multiple columns
    # each column is all data for one city
    # breaking the data into year wise data for each city
    years = np.arange(1990, 2023)
    df['Date'] = pd.to_datetime(df['Date'])
    df['year'] = df.Date.apply(lambda x: x.year)

    # selecting fuel type
    fuel_type = fuel_types[0]
    df = df[df['Fuel Type'] == fuel_type]

    # segregating yearly fuel prices
    data_yearly: list = []
    sizes: list = []
    for year_ in years:
        df_ = df.where(df.year == year_).dropna()
        df_ = df_[cities]
        df_.columns = [year_]
        # df_.reset_index(drop=True,inplace = True)
        data_yearly.append(df_)
        sizes.append(df_.index.shape[0])

    # make all dfs equal in size
    data_yearly_equal: list = []
    max_size = max(sizes)
    for df_ in data_yearly:
        size_diff = max_size-df_.index.shape[0]
        if size_diff:
            col_name = df_.columns
            df_temp = pd.DataFrame(np.zeros(size_diff), columns=col_name)
            df_ = df_.append(df_temp)
        df_.reset_index(drop=True, inplace=True)
        data_yearly_equal.append(df_)

    # combining all dataframes into yearwise, rows,column = week,year
    df_comb = pd.concat(data_yearly_equal, axis=1)

    # plotting
    ycol = df_comb.columns.tolist()
    df_comb['x'] = df_comb.index.tolist()
    xcol = 'x'
    fig = px.line(df_comb,
                  x=xcol,
                  y=ycol,
                  title='Oil in Canada')
    fig.show()
