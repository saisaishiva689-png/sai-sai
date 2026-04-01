marks = int(input("Enter the marks of the student = "))
if marks < 0 or marks >100:
    print("enter the valid marks")
elif marks >= 90:
    print("Grade A ")
elif marks  >= 80 :
    print("Grade B ")
elif marks >= 70 :
    print("Grade C ")
elif marks >= 60 :
    print("Grade D")
elif marks >= 50 :
    print("Grade E")      
else :
    print("Fail")