#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hi WELCOME TO PYTHON INTRO"
'''
In this Python class, we will learn about a few basics of python!

First demo the "Script, command line and Jupyter notebook of executing the Python :-)"

'''


# In[16]:


print('hello world')


# In[4]:


#there is an extra "", end of line for intepreter is not appropriate
if 5 > 2:
 print("Five is greater than two!"")


# In[3]:


#indentation is not proper
if (5>2):
print("5 is gt than 2")


# In[5]:


#print indentation is correct and it has executed well
if (5 > 2):
 print("5 is gt than 2")


# In[8]:


#This is a comment - Single Line comment
print("Hello, World!")


# In[7]:


''' A Multiline comment
Hi how are u
'''
"""This is a comment
written in
more than just one line
"""
print("Hello, World!")


# In[8]:


'''
None is not equal to “ ” or 0 
None can help in identifying conditions that are false,,,
not None is true
'''


none


# In[19]:


#it's  None    and not none!
None


# In[10]:


#There is a type None
print(type(None))


# In[20]:


'''
https://www.w3schools.com/python/ref_keyword_none.asp

The None keyword is used to define a null value, or no value at all.

None is not the same as 0, False, or an empty string. 

None is a data type of its own (NoneType) and only None can be None.

'''

x = None

print(x)


# In[21]:


print(None == None)
print(None is None)


# In[22]:


print(None == False)


# In[23]:


print(None != 50)


# In[25]:


#Invalid Syntax!

print(!None)


# In[26]:


# Is None True or False or if not, what is it?
x = None

if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")


# In[27]:


x = 5
y = "John"
print(x)
print(y)


# In[28]:


type(x)


# In[30]:


'''
Key Board shorcuts

shift enter to run the current cell
alt enter for run and generate new cell
control enter to run current cell
'''


# In[34]:


x = "Sally"


# In[ ]:





# In[35]:


type(x)


# In[36]:


#Multiple variable Assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# In[37]:


x =y=z= "Orange"
print(x)
print(y)
print(z)


# In[38]:


#Concatination
x = "Orange" + "Banana"
print(x)


# In[43]:


#'hello' is the same as "hello". The triple quotation mark can span multiple lines of text.
#The triple quotation mark can span multiple lines 
print('hello' == "hello")


# In[44]:


#String Slicing Operations

'''
Method 1: Using the slice() method

The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).

Syntax:

slice(stop)
slice(start, stop, step)
Parameters: start: Starting index where the slicing of object starts. 
stop: Ending index where the slicing of object stops.
step: It is an optional argument that determines the increment between each index for slicing. 
Return Type: Returns a sliced object containing elements in the given range only. 

# Python program to demonstrate
# string slicing
 
# String slicing
String = 'ASTRING'
 
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
 
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])


or Method 2 is  Using the List/array slicing  [ :: ]  method

arr[start:stop]         # items start through stop-1
arr[start:]             # items start through the rest of the array
arr[:stop]              # items from the beginning through stop-1
arr[:]                  # a copy of the whole array
arr[start:stop:step]    # start through not past stop, by step


'''
b = "Hello,World!"
print(b[2:7])


# In[47]:


# Python program to demonstrate
# string slicing
 
# String slicing
String = 'ASTRING'
 
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
 
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])


# In[48]:


name="Mahmood"
print(name[2:-1])


# In[49]:


name="Mahmood"
print(name[2:6])


# In[50]:


b = "HelloWorld!"
print(b[:5])


# In[51]:


b = "HelloWorld!"
print(b[0:5])


# In[52]:


b = "HelloWorld!"
print(b[2:])


# In[54]:


print(b[0])


# In[56]:


X = "my name is : {} and I am {} years old"
print(X.format("Abdulla", 19))


# In[57]:


x=5
print(x*3)


# In[58]:


print(25/5)


# In[59]:


print(25//5)


# In[60]:


x=5
print(x**3)


# In[61]:


x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


# In[62]:


x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


# In[63]:


#identity operators is and isnot
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# In[64]:


#Lists -is ordered and mutable"
mylist = ["apple", "banana", "cherry"]
mylist


# In[65]:


#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[66]:


'''
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

List literals are written within square brackets [ ]. Lists work similarly to strings 
use the len() function and square brackets [ ] to access data, with the first element at index 0.

'''


# In[67]:


#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# In[68]:


#Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[69]:


#Loop in lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[73]:


#Append

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)




# In[74]:


a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
print(b)


# In[75]:


'''
TUPLES
A tuple is a collection which is ordered and immutable. In Python tuples are written with round brackets.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# In[ ]:


'''
The key difference between tuples and lists is that while tuples are immutable objects, lists are mutable. 
This means tuples cannot be changed while lists can be modified. 
Tuples are also more memory efficient than the lists

'''


# In[76]:


#Slicing operations using tuples as we do with strings

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# In[77]:



#Looping! always helps to traverse through the list!

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# In[78]:


myTuple = ("apple","banana","cherry","apple")
print(myTuple.index("banana")) 


# In[98]:


#Tuples are Immutable and does not support item creation
myTuple = ("apple","banana","cherry")
myTuple[3]="Orange"
print(myTuple) 


# In[85]:


#A few more in List
mylist = ["apple","banana","cherry"]
mylist[2]=["Orange"]
#Try this too 
#mylist[3]="Musk Melon"
print(mylist) 


# In[86]:


'''
A set is a collection of unique items which is unordered and unindexed 
n Python, we create sets by placing all the elements inside curly braces {} , separated by comma. 
A set can have any number of items and they may be of different types (integer, float, tuple, string etc.).
But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

'''

thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[87]:


#Travesing through the items in the set!
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[88]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[89]:


#An example of set using list, which is mutable... 
#cannot be an element and will throw error

thisset = {"apple", "banana", "cherry", ["list"]}


# In[91]:


#An example of set using tuple, which is immutable... 
#can be an element and will not throw error

thisset = {"apple", "banana", "cherry", ("tuple")}
print(thisset)


# In[94]:


#An example of set using set, which is immutable... 
#cannot be an element and will throw error

thisset = {"apple", "banana", "cherry", {"tuple"}}
print(thisset)


# In[95]:


'''
Dictionaries-A dictionary is a key-value pair collection which is unordered, mutable and indexed. 
written in 

dictname= {
    "Key1":"Value1",
    "Key2":"Value2"
}

print(dictname)


Very similar to json format!
'''


# In[97]:


# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)


# In[96]:


'''
Dictionaries are written with curly brackets, and have keys and values:

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[98]:


#Dictionaries cannot have two items with the same key;
#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# In[112]:


'''Nested Dictionaries
A dictionary can contain dictionaries, 

this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

myfamily


# In[110]:


'''if you want to add three dictionaries into a new dictionary:

Example
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:



'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# In[113]:


myfamily


# In[99]:


#Python Functions

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Noora", "Sini")


# In[100]:


#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Saba", "Sini", "Noora")


# In[101]:


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# In[102]:


'''
With the break statement we can stop the loop before it has looped through all the items:

Example
Exit the loop when x is "banana":
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


# In[103]:


'''
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.

'''

for x in range(6):
  print(x)


# In[104]:


'''
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:
'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# In[ ]:




