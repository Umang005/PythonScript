import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\StudentsWithPerCenatges.csv")
df1 = df.sort_values(by='Percentage',ascending=False)
df1["Rank"] = df1["Percentage"].rank(ascending=False)
print(df1)
df2=df1.head(3)
print(df2)
df2.to_csv(r"C:\Users\Ashish\Documents\USE CASE\TopperList.csv",index=False)
