import pandas as pd
import sys
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv")
df["Percentage"]=(df["Maths"]+df["Physics"]+df["Chemistry"])*0.3
print(df)
Student_name=sys.argv[1]
Subject_name=sys.argv[2]
Deducted_Marks=sys.argv[3]

for i in range(0,len(df["Student Name"])):
    if df.loc[i,"Student Name"]==Student_name:
        df.loc[i,Subject_name]=df.loc[i,Subject_name]-int(Deducted_Marks)
#df.loc[Student_name,Subject_name]=df.loc[Student_name,Subject_name]-Deducted_Marks
print(str(Student_name)+" : "+ str(Deducted_Marks) +"Marks are deducted in subject "+str(Subject_name))
print(df)
GR_Subject=sys.argv[4]
fig = plt.figure(figsize = (10, 5))
plt.bar(df["Student Name"],df[GR_Subject],color='maroon',width=0.4)

plt.xlabel("Students Name")
plt.ylabel("Marks Obtained in "+str(GR_Subject))
plt.title("Students comparision ")
plt.show()
df.to_csv(r"C:\Users\Ashish\Documents\USE CASE\Student.csv",index=False)



