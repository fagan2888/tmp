
import pandas as pd

df = pd.DataFrame({'a':[1,2,4],'b':[2,3,4]})
#df['c'] = df['a'].rank()
print(df)
print(df.shape[1])
print(df.iloc[:,1])
