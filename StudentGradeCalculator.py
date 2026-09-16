name=input("enter the name:")
sub1=int(input("enter marks of sub 1"))
sub2=int(input("enter marks of sub2 "))
sub3=int(input("enter marks of sub 3"))
average=(sub1+sub2+sub3)/3
print(average)
if average>=50:
    print("gradeA")
elif average>=35:
    print("gradeB")
else:
    print("fail")