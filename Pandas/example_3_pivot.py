import pandas as pd
import numpy as np

data = {'human':['man', 'woman', 'man', 'man', 
                 'woman', 'man', 'woman', 'man', 'man'],
        'status':['poor', 'rich', 'rich', 'poor', 
                 'poor', 'rich', 'rich', 'poor', 'poor'],
        'height':[178, 165, 190, 174, 160, 180, 170, 182, 170],
        'weight':[70, 60, 90, 67, 58, 75, 65, 80, 65]}

df = pd.DataFrame(data)

df = df.pivot_table(index = ['human'],
                    columns = 'status',
                    values = ['height', 'weight'],
                    aggfunc = np.mean)
print(df)