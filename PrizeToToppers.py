import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\TopperList.csv")
for i in range(0,3):
    if df.loc[i,"Rank"]==1:
      print(str(df.loc[i,"Student Name"])+" ="+ "Gold")
    elif df.loc[i,"Rank"]==2:
      print(str(df.loc[i,"Student Name"])+" ="+ "Silver")
    elif df.loc[i,"Rank"]==3:
      print(str(df.loc[i,"Student Name"])+" ="+ "Bronze")

