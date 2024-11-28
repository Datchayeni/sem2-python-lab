#area of rectangle
l=int(input("Enter the lenght of the rectangle:"))
b=int(input("Enter the breath of the rectangle:"))
area=l*b
print("Area of the rectangle=",area)

#area of square
s=int(input("Enter the side of the square:"))
a=s*s
print("Area of the square=",a)

#area of circle
r=int(input("Enter the side of the radius of the circle:"))
c=(3.14)*r**2
print("Area of the circle=",c)

#area of triangle
ba=int(input("Enter the side of the base of the triangle:"))
h=int(input("Enter the side of the height of the triangle:"))
t=1/2*ba*h
print("Area of the triangle=",t)

#fibo
n=int(input("enter the number:"))
a,b=0,1
count=0
while count<n:
    a,b=b,a+b
    count+=1
    print(a,end=" ")

    

