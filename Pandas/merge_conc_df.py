# https://newtechaudit.ru/pandas-merge-join-concatenate/

import pandas as pd

df2 = pd.DataFrame({'A1': ['43', '3', '80', '5'],
                     'B1': ['B0', 'B1', 'B5', 'B3'],
                     'C1': ['C4', 'C5', 'C6', 'C7'],
                     'D1': ['D4', 'D5', 'D6', 'D7']})

df1 = pd.DataFrame({'A': ['5', '87', '42', '43'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

df3 = df1.join(df2)

# df4 = df1.merge(df2, left_on='B', right_on='B1', how ='inner')
df4 = df1.merge(df2, left_on='B', right_on='B1', how ='outer')
# df4 = df1.merge(df2, left_on='B', right_on='B1', how ='left')
# df4 = df1.merge(df2, left_on='B', right_on='B1', how ='right')

df5 = pd.concat([df1, df2], sort=False, axis=1)

df6 = df1.append(df2, sort=False)

print(df3,'\n')
print(df4,'\n')
print(df5,'\n')
print(df6)