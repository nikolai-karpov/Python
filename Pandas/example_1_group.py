import pandas as pd
import numpy as np
from collections import Counter

data = {'human':['man', 'woman', 'man', 'man', 
                 'woman', 'man', 'woman', 'man', 'man'],
        'height':[178, 165, 190, 174, 160, 180, 170, 182, 170],
        'weight':[70, 60, 90, 67, 58, 75, 65, 80, 65]}

df = pd.DataFrame(data)

print(df.groupby('human')['height'].agg([min, np.median, max]))
print()
print(df.groupby('human')['weight'].agg([min, np.median, max]))

cnt = Counter(data['human'])
print(dict(cnt))