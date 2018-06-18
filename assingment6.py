#Q.1print 10 integer from user
for x in range (10):
 x=int(input("enter ineger number"))
 print("entered value",x)
#Q.2 write an infinite loop
i=1
while i<10:
    print("hello world")
print(i)
#Q.3 square of user defined list
numbers=[]
for i in range(0,5):
    num=int(input("enter the list "))
    numbers.append(num)
print("list is",numbers)
squares=[]
for num in numbers:
    sq=num*num
    squares.append(sq)
print(squares)


#Q.4 list containing value of int,string,float
l=[1,2.2,'abc',3,3.9,'jkl']
for i in l:
    print("the list is",i,"is",str(type(i)))

#Q.5 EVEN ODD NUMBER BETWEEN 1 TO 10.
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#Q.6 print star.
i=1
while i<=4:
    print("*"*i)
    i=i+1
#Q.7 Create a user defined dictionary.
d={'dream':333,'destiny':777,'feeling':999}
for key in d.keys():
      print(key,d[key])

#Q.8 list operation like searching and deletion.
l=[85,54,78,98]
num==int(input("the no which u want in list"))
for i in l:
     if i==num:
         print("value found")
         l.remove(i)
print(l)         
