import pandas as pd

def to_merge(df_to_merge, csv_name):
    df = pd.read_csv('breit30.csv')
    df2 = pd.read_csv(df_to_merge)
    

    df.dt = pd.to_datetime(df.iloc[:,1])
    df2.dt = pd.to_datetime(df2.iloc[:,1])
    
    concat_df = pd.concat([df,df2])
    concat_df = concat_df.sort_values(by=['dt'], ascending = False)
    concat_df = concat_df.drop(columns=['Unnamed: 0'])
    return concat_df.to_csv(f'{csv_name}.csv')

to_merge('11_11_10_26_55update.csv', 'breit31')




"""df = pd.read_csv('breit24.csv')
df2 = pd.read_csv('324_510.csv')


df.dt = pd.to_datetime(df.iloc[:,1])
df2.dt = pd.to_datetime(df2.iloc[:,1])

concat_df = pd.concat([df2,df])
concat_df = concat_df.sort_values(by=['dt'], ascending = False)
concat_df = concat_df.drop(columns=['Unnamed: 0'])
concat_df.to_csv(f'breit25.csv')"""







""" df = pd.read_csv('CM1_10.csv')
df2 = pd.read_csv('CM11_56.csv')
df3 = pd.read_csv('CM57_80.csv')
df4 = pd.read_csv('CM81_105.csv')
df5 = pd.read_csv('CM105_150.csv')
df['dt'] = pd.to_datetime(df.iloc[:,1])
df2['dt'] = pd.to_datetime(df2.iloc[:,1])
df3['dt'] = pd.to_datetime(df3.iloc[:,1])
df4['dt'] = pd.to_datetime(df4.iloc[:,1])
df5['dt'] = pd.to_datetime(df5.iloc[:,1])
concat_df = pd.concat([df,df2, df3, df4, df5])
concat_df = concat_df.sort_values(by=['dt'], ascending = False)
concat_df = concat_df.drop(columns=['Unnamed: 0'])
concat_df.to_csv('CMall.csv')



df.dt = pd.to_datetime(df.iloc[:,1])
df2.dt = pd.to_datetime(df2.iloc[:,1])

concat_df = pd.concat([df,df2])
concat_df = concat_df.sort_values(by=['dt'], ascending = False)
concat_df = concat_df.drop(columns=['Unnamed: 0'])
return concat_df.to_csv(f'{csv_name}.csv') """