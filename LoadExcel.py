import pandas as pd
import sys
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv")
df["Percentage"]=(df["Maths"]+df["Physics"]+df["Chemistry"])*0.3
print(df)
df.to_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv",index=False)
name=sys.argv[1]
fig = plt.figure(figsize = (10, 5))
plt.bar(df["Student Name"],df[name],color='maroon',width=0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

