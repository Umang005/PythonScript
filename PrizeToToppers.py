import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv")
for i in range(0,3):
    if 1<=df.loc[i,"Rank"]<2:
      print(str(df.loc[i,"Student Name"])+" ="+ "Gold")
    elif 2<=df.loc[i,"Rank"]<3:
      print(str(df.loc[i,"Student Name"])+" ="+ "Silver")
    elif 3<=df.loc[i,"Rank"]<4:
      print(str(df.loc[i,"Student Name"])+" ="+ "Bronze")


#fig = plt.figure(figsize = (10, 5))
#plt.bar(df["Student Name"],df["Rank"],color='maroon',width=0.4)

#plt.xlabel("Students Name")
#plt.ylabel("Rank Obtained")
#plt.title("Students Ranking ")
#plt.show()
