print("Enter 'c' to convert from Celsius to Farenheit")
print("Enter 'f' to convert from farenheit to Celsius")
choice=input("Enter your choice")
if choice=='c':
    celsius=float(input("Enter temperature in Celsius"))
    farenheit=(celsius*9/5)+32
    print('%.2f Celsius is:%0.2f Farenheit'%(celsius,farenheit))
elif choice=='f':
    farenhiet=float(input("Enter temperature in Farenhiet"))
    celsius=(farenhite+32)*5/9
    print('%.2f Farenheit is:%0.2f Celsius'%(farenheit,celsius))
else:
    print("invalid Input")



a=int(input("Enter marks obtained in subject 1:"))
b=int(input("Enter marks obtained in subject 2:"))
c=int(input("Enter marks obtained in subject 3:"))
d=int(input("Enter marks obtained in subject 4:"))
e=int(input("Enter marks obtained in subject 5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")
