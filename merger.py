import pandas as pd

def to_merge(df_to_merge, csv_name):
    df = pd.read_csv('breit16.csv')
    df2 = pd.read_csv(df_to_merge)
    

    df.dt = pd.to_datetime(df.iloc[:,1])
    df2.dt = pd.to_datetime(df2.iloc[:,1])
    
    concat_df = pd.concat([df,df2])
    concat_df = concat_df.sort_values(by=['dt'], ascending = False)
    concat_df = concat_df.drop(columns=['Unnamed: 0'])
    return concat_df.to_csv(f'{csv_name}.csv')

to_merge('11_02_09_51_50update.csv', 'breit17')