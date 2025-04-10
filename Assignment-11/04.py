import pandas as pd

data ={
    'John': [True, False, True, True, False, False, True, False, True, True],
    'Judy': [True, True, False, True, False, True, True, False, False, True]
}

df = pd.DataFrame(data)

df['party'] = df['John'] & df['Judy']

daystillparty = [None] * len(df)
nextpartyindex = None

for i in reversed(range(len(df))):
    if df.loc[i, 'party']:
        daystillparty[i] = 0
        nextpartyindex = i
    elif nextpartyindex is not None:
        daystillparty[i] = nextpartyindex - i
    else:
        daystillparty[i] = None

df['daystillparty'] = daystillparty
print(df)