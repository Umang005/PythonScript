import pandas as pd

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv")
df["Percentage"]=(df["Maths"]+df["Physics"]+df["Chemistry"])*0.3
print(df)
df.to_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv",index=False)