studdata={'Abhishek':92.45,'Akash':89.34,'Akshata':90.45,'Anjali':78.32,'Ankita':80.56,'Anurag':89.90}
Name=input("Enter the student's name: ")
Mark=studdata.get(Name)
if Mark==None:
    print("Student not found.")
else:
    print(f"{Name}'s marks: {Mark} ")
