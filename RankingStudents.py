import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv")
df1 = df.sort_values(by='Percentage',ascending=False)
df1["Rank"] = df1["Percentage"].rank(ascending=False)
print(df1)
df1.to_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv",index=False)
