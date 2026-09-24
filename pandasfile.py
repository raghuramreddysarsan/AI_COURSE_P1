import pandas as pd
df = pd.read_csv('digital_behaviour.csv')
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.shape)
print(df.columns)
print(df[["Instagram_Minutes","Study_Minutes"]].describe())
print(df[["Date","Instagram_Minutes"]])
col = ["Instagram_Minutes","Study_Minutes"]
df[col]
print(df["Instagram_Minutes"].sum())
print(df["Instagram_Minutes"].mean())
print(df["Instagram_Minutes"].max())
print(df[df["Instagram_Minutes"]>100])

