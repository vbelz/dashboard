import pandas as pd
import os
import re

path = './namesbystate/'

list_files = os.listdir(path)

pattern = '[A-Z]*.TXT'
df_merge = pd.DataFrame()

#Read all files per year:
for i in range(len(list_files)):
    if re.match(pattern,list_files[i]) :
            df=pd.read_csv(path+f'{list_files[i]}', header=None, names=['State','Sex','Year','Names','Count_states'])
            df_merge = pd.concat([df_merge,df])

#Create a unique index for primary key:
df_merge['id'] = list(range(df_merge.shape[0]))
df_merge.set_index('id',inplace = True)

#Create a total sum per country per group (Names,Year)
df_merge['Count_country'] = df_merge.groupby(['Year','Names'])['Count_states'].transform(sum)

df_merge.to_csv('babynames_db.csv', header=None)