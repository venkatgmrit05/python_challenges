# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:06:46 2021

@author: umave
"""


import pandas as pd

# importing data
data_file = r'.\data_cleaning_challenge.csv'

df_data = pd.read_csv(data_file)
splitter = ',,,,,,,,,,\n,,,,,,,,,,' #based on a quick observation of the data

with open(data_file,'r') as file:
    data_txt = file.read()
    
# splitting data  
data_txt_tokens =   data_txt.split(splitter)


#for a single piece of repeating data 
#re-organizing data into meaningful/structured shape

list_dfs = []
for original_token in data_txt_tokens[:]:
    # original_token = data_txt_tokens[0]
    #the following code will be looped over each token in data_txt_tokens
    splitter2 = ',,,,,,,,\n'
    token_label,*_,token = original_token.split(splitter2)
    token_lines = token.split('\n')
    token_row_dict = {}
    token_dict = {}
    for num,line in enumerate(token_lines):
        line_tokens = line.split(',')
        token_dict[num] = pd.Series(line_tokens)
    df = pd.DataFrame(token_dict)
    df2 = df.copy()
    df.columns = df.loc[0,:]
    df.drop(labels = [0],inplace = True)
    df.dropna(inplace = True,
              how = 'all', 
              axis = 1)
    invalid_columns = [name  for name in df.columns if not name]
    df.drop(columns = invalid_columns,inplace = True)
    
    #re-factoring /re-shaping data
    df2 = df.copy()
    df2 = df2.T
    df2.columns = df2.loc['Row Type',:]
    df2.drop(labels = ['Row Type'],inplace = True)
    data_labels = token_label.split(',')
    data_labels = [item.split(':') for item in data_labels]
    data_labels = [item for item in data_labels if len(item) == 2]
    data_labels = {k:v for k,v in data_labels}
    
    for key in data_labels:
        df2[key]= data_labels[key]
    
    list_dfs.append(df2)
    
list_dfs_indexed = [_df for _df in list_dfs]
list_dfs_indexed = [_df.reset_index() for _df in list_dfs]
cols = list_dfs_indexed[0].columns
list_dfs_indexed = [_df.drop(columns=['',]) for _df in list_dfs_indexed]

list_cleaned_dfs = []
for _df in list_dfs_indexed:
    old_columns = _df.columns
    old_columns = [str(item) for item in old_columns]
    old_columns = [item.strip() for item in old_columns]
    _df.columns = old_columns
    list_cleaned_dfs.append(_df)

dff = pd.DataFrame()
dff = dff.append(list_cleaned_dfs)
df_final = dff.copy()

# =============================================================================
# validation  that no data is incorrectly left out.
# dff Dataframe must /should have similar if not exact same amount of rows
# when all the meta data rows are removed from the original table without any data cleaning
 # =============================================================================

df_data2 = df_data.dropna(how = 'all')

indices_to_drop = []
for ind in df_data2.index:
    row_data = df_data2.loc[ind,:].tolist()
    if 'first name: Person' in row_data or 'Row Type' in row_data:
        indices_to_drop.append(ind)
        
df_data3 = df_data2.drop(labels = indices_to_drop)
df_data3.reset_index(drop= True,
                     inplace = True)


# =============================================================================
# condition_of_no_data_loss = dff.shape[0] == df_final.shape(0)
# =============================================================================
