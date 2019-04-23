import pandas as pd
import numpy as np
df = pd.read_csv(r'/Users/huangkai/Desktop/fra.out',sep='\t',engine='python')
col = df.columns.values.tolist()
delete_col = []
for i in col[1:]:
    if 'O' not in i:
        delete_col.append(i)
new = df.drop(columns=delete_col)
new.to_csv('O_element.out',index=0)

