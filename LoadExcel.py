import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Book.csv")
df["Percentage"]=(df["Maths"]+df["Physics"]+df["Chemistry"])*0.3
print(df)
df.to_csv(r"C:\Users\Ashish\Documents\USE CASE\StudentsWithPerCenatges.csv",index=False)