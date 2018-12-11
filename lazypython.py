
# -*- coding: cp1254 -*- 
#its for turkish character



#print('hi world')"

#standart veri tipleri
#Numbers
#String
#List
#Tuple
#Dictionary

#desteklenensayitiokers
#int (signed integers)
#long (long integers, they can also be represented in octal and hexadecimal)
#float (floating point real values)
#complex (complex numbers)


#word = 'word'
#sentence = "This is a sentence."
#paragraph = """This is a paragraph. It is
#made up of multiple lines and sentences."""


#degiskentanimlama
#counter = 100          # An integer assignment
#miles   = 1000.0       # A floating point
#name    = "John"       # A string

#print(counter)
#print (miles)
#print (name)

#cokludegiskentanimlama
#a,b,c = 1,2,"john"
#a = b = c = 1


#x = 1
#y = 2.8
#z = 1j

#print(type(x))
#print(type(y))
#print(type(z))

#y = int(2.8) # y will be 2
#y = float(2.8)   # y will be 2.8
#x = str("s1") # x will be 's1'
#y = str(2)    # y will be '2'



#degiskensilme
#a = "tasdest"
#del  a
#a = "best"
#print a


#a = "Hello, World!"
#print(a.lower())
#print(a.upper())
#print(a.replace("H", "J"))
#print(a.split(","))

#kelimeisleme
#word ="secilen kelime hello world olsun"
#print(word[15:26])
#hello world
#print(word[-30:])
#cilen kelime hello world olsun
#print(word[15:])
#hello world olsun
#print(word[15:20] +' the' + word[20:26] )
#hello the world


#<!--    listsarrays  ---->



#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


#thislist = ["apple", "banana", "cherry"]
#print(thislist)
#print(thislist[1])
#thislist[1] = "blackcurrant"
#print(thislist)

#for x in thislist:
  #print(x)

#if "apple" in thislist:
 #print("Yes, 'apple' is in the fruits list"
#print(len(thislist))
#thislist.append("orange")
#print(thislist)
#.insert(1, "orange")
#print(thislist)
#thislist.remove("banana")
#thislist.pop()
#thislist.clear()
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#print(thislist)




#squares = [1, 4, 9, 16, 25]
#print(squares)
#[1, 4, 9, 16, 25]
#print(squares[-1])
#25
#print(squares + [36, 49, 64, 81, 100])
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#squares.append(123)
#print(squares + [36, 49, 64, 81, 100])
#squares[3]=88 4.rakam 16 yerine 88 olur
#print(squares)
#[1, 4, 9, 88, 25]
#print(len(squares))
#5


#a = [["a","b","c",],["d","e"],["f","g","h"]]
#print(a[2][1])
#g

#nest lists
#a = ["a","b","c",[1,3,4]]
#b= [[7,5,4],1,2,3]
#print(a[3],b[0])

#<!--    listsarrays  ---->


#<!--    ifelse ---->
""" 
a = 33
b = 200
if b > a:
 print("b is greater than a")

a = 33
b = 200
if b > a:
print("b is greater than a")


#boşluğa dikkat et
 

a=33
b=123
c=123213
if a < b and a < c:
	print("whatsuupp")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#<!--    ifelse ---->


#<!--    while---->
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
   print('bulshit')
  i += 1

#a, b = 0, 1
#while b < 10:
#	print(b*a)
#	a, b = b, a-b

#i = 1
#while i < 6:
#  print(i)
 # i += 1


#<!--    while---->


#<!--    for ---->
veriler =['test','test1','test3']
for x in veriler:
  if x == "test1":
    continue
  print(x)
  #test,test3

#2 den 30 a kadar sıralama ayrıca 5 er 5 er artar
for x in range(2, 30,5):
  print(x) 
	

	adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

//geri dönüşümlü fonksiyon
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecu
	rsion Example Results")
tri_recursion(4)
Recursion Example Results
1
3
6
10

#<!--    for ---->
#<!--fonksiyonlar----> 
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))




#<!--   lambda---->
A lambda function is a small anonymous function.
lamba birçok argüman için kullanılabilir ancak
not tek bir argüman için tek bir eşitlik için kullanılabilir
x = lambda a: a + 10
print(x(5))


y = lambda a: a + 10
print(y(5))


#<!--   lambda---->
#<!--fonksiyonlar----> 

#<!--arrays----> 
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
setlerdeki bütün fonskiyonlar aynen geçerki



#<!--arrays---->

<--! OOP -->

class Car:

    

    # Initializer / Instance Attributes
    def __init__(self, name, model):
        self.name = name
        self.model= model

    # instance method
    def description(self):
        return "The {} has {} models ".format(self.name, self.model)

    # instance method
    def fastlimit(self, properties):
        return "{} has {}  speed limit".format(self.name,properties)

# Instantiate the Dog object
Tesla = Car("Tesla", "electrics car")

# call our instance methods
print(Tesla.description())
print(Tesla.fastlimit(123213))
<--! OOP -->
<--! yineleciler ve yinelenebilir -->
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
b,a


mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
 hepsini sıralar
<--! yineleciler ve yinelenebilir -->

<!-- moduls -->

import lazypymodule
lazypymodule.greeting("Jonathan")

a = lazypymodule.robot["age"]
print(a)


from lazypymodule import robot
print (robot["age"])

<!-- moduls -->



<!-- time -->
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x.strftime("%A"))

<!-- time -->


<!-- json -->
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

<!-- json -->

<!-- dosya işlemleri -->
f = open("demofile.txt",r)
print(f.read())
print(f.read(5))

f.write("Now the file has one more line!")


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


  //folder os.rmdir("myfolder")

<!-- dosya işlemleri -->
"""
