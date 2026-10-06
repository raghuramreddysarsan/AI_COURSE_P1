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
avg=print(df["Instagram_Minutes"].mean())
print(df["Instagram_Minutes"].max())
print(df[df["Instagram_Minutes"]>100])
print(df[df["Study_Minutes"]>180])
print(df[df["Instagram_Minutes"]>df["Study_Minutes"]])
print(df["Instagram_Minutes"]>avg)
ab=df["Instagram_Minutes"].sort_values(ascending = False)
print(ab)
top_five = df.sort_values(by="Instagram_Minutes",ascending=False).head(5)
print(top_five[["Date", "Instagram_Minutes"]])
df["Total_time"] = df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"]
print(df[["Date","Total_time"]].head())
df["Screen_Hours"] = df["Total_time"] / 60
df["Digital_Balance"] = df["Study_Minutes"]/df["Total_time"]
print(df[["Date","Screen_Hours","Total_time"]])
df["Day_type"] = "Normal"
df.loc[(df["Total_time"] > 300), "Day_type"] = "Heavy"
print(df[["Date", "Total_time", "Day_type"]].head(8))


#1
i,w,l,y = (df["Instagram_Minutes"].sum(), df["WhatsApp_Minutes"].sum(),df["LinkedIn_Minutes"].sum(),df["YouTube_Minutes"].sum())
print(i,w,l,y)

#2
print(max(i,w,l,y))

#3
print((df["Day_type"]=="Heavy").sum())

#4
print(df[df["Study_Minutes"]==(df["Study_Minutes"].max())])

#5
print(df[df["Total_time"]==(df["Total_time"].max())]["Study_Minutes"])

#6
print(df["Digital_Balance"].mean())

