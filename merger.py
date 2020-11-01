import pandas as pd

def to_merge(df_to_merge, csv_name):
    df = pd.read_csv('breit12.csv')
    df2 = pd.read_csv(df_to_merge)
    

    df.dt = pd.to_datetime(df.iloc[:,1])
    df2.dt = pd.to_datetime(df2.iloc[:,1])
    
    concat_df = pd.concat([df,df2])
    concat_df = concat_df.sort_values(by=['dt'], ascending = False)
    concat_df = concat_df.drop(columns=['Unnamed: 0'])
    return concat_df.to_csv(f'{csv_name}.csv')

to_merge('10_31_update.csv', 'breit13')



df = pd.read_csv('breit11.csv')
df2 = pd.read_csv('1_10.csv')
df2 = df2.iloc[0:75,:]

df.dt = pd.to_datetime(df.iloc[:,1])
df2.dt = pd.to_datetime(df2.iloc[:,1])

df2.tail()

concat_df = pd.concat([df,df2])
concat_df = concat_df.sort_values(by=['dt'], ascending = False)
concat_df = concat_df.drop(columns=['Unnamed: 0'])
concat_df.to_csv(f'breit12.csv')