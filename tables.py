#1.write a program to print the multiplication of the table of the no. by using FOR loop.

num = int(input("enter the number:"))
for i in range(1,11):
   # print(str(num)+"X"+str(i)+"="+str(i*num))   #OR
    print(f"{num}X{i}={num*i}") # f string

#2.write a program to print the reversed multiplication of the table of any no. by using FOR loop.

num = int(input("enter the number:"))
for i in range(10,0,-1):
    print(f"{num}X{i}={num*i}")    