#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys


# In[ ]:


a Python scope determines where in your program a name is visible.
Python scopes are implemented as dictionaries that map names to objects. 
These dictionaries are commonly called namespaces.
These are the concrete mechanisms that Python uses to store names. 
They’re stored in a special attribute called .__dict__.


# In[3]:


sys.__dict__.keys()


# In[4]:


x=30
def my_func():
	x=40
	return x
print(x)


# In[5]:


x=30
def my_func():
	x=40
	return x
my_func()
print(x)


# In[6]:


x=30
def my_func():
	x=40
	return x
x = my_func()
print(x)


# In[7]:


'''
Create a class named MyClass, with a property named x:

'''

class MyClass:
  x = 5


# In[8]:


'''
Create an object named p1, and print the value of x: '''

p1 = MyClass()
print(p1.x)


# In[12]:


class Animal:
    


# In[10]:


class Animal:
	pass
#this is an empty class

#class definitions cannot be empty, but if you for some reason have a class definition with no content, 
#put in the pass statement to avoid getting an error.


# In[24]:


'''
The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:

'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and I am",self.age)

p1 = Person("Sini", 60)
p1.myfunc()


# In[28]:


'''
Special method:

All classes have a function called __init__(), which is always executed when the class is being initiated.
The __init__() function is called automatically every time the class is being used to create a new object.


Create a class named Person, use the __init__() function to assign values for name and age:

'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# In[25]:


'''
Special Methods

+++++++++++++++++++++++++++


The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned

'''

#The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


# In[26]:


#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


# In[30]:


del p1


# In[31]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


# In[32]:


del p1.age


# In[33]:


print(p1.age)


# In[34]:


del p1


# In[35]:


print(p1)


# In[37]:


'''
__repr__  method returns the string representation of an object.

By default, the output contains the memory address of the person object. 
To customize the string representation of the object, you can implement the __repr__ method as given below in comments


'''


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'
        '''
    
person = Person("John", "Doe", 25)
print(repr(person))


# In[38]:


'''
__dict__ already seen

__ name__  The __name__ attribute returns the name of the module.
By default, the name of the file (excluding the extension .py) is the value of __name__attribute.
'''
import math
math.__name__


# In[39]:


math.__dict__


# In[ ]:


'''
What is __ bases __ in Python?
Python provides a __bases__ attribute on each class that can be used to obtain a list of classes the given class inherits.

The __bases__ property of the class contains a list of all the base classes that the given class inherits.

Check out and explore!

'''


# In[43]:


'''

Functions to Manage Attributes

getattr() Syntax:

The syntax of getattr() method is:

getattr(object, name of attribute)


The above syntax is equivalent to:

object.name

'''

class Student:
  marks = 99
  name = 'Ahmed'

person = Student()

name = getattr(person, 'name')
print(name)

marks = getattr(person, 'marks')
print(marks)


# In[44]:


'''
U can provide default value to a getattribute

'''

class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
print('The sex is:', getattr(person, 'sex'))


# In[51]:


'''
Activity - Try by urself

'''
class Car():
	total_cars = 0
	def __init__(self, make, year):
		self.make = make
		self.year= year
		Car.total_cars += 1

my_car = Car(make = "Toyota", year=1992)
print(type(my_car))
print(my_car.make)
print(Car.total_cars)


# In[92]:


'''
=================
INHERITANCE
+++++++++++++++++++++
'''

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  


# In[94]:


'''
Multi-Level inheritance

class class1:  
    <class-suite>   
class class2(class1):  
    <class suite>  
class class3(class2):  
    <class suite>  
    

'''
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
        
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
        
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
        
d = DogChild()  

d.bark()  
d.speak()  
d.eat()  


# In[95]:


'''
=======================
Multiple inheritance
========================

class Base1:  
    <class-suite>  
  
class Base2:  
    <class-suite>  
 
  
class Derived(Base1, Base2):  
    <class-suite>  

'''

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
    
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
    
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
    
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  


# In[96]:


'''
====================
METHOD OVERRIDING
=====================

'''

class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak()  


# In[101]:


'''
Inheritance:

Create a class named Person, with firstname and lastname properties, and a printname method:


'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
      pass




#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()


# In[54]:




'''So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

Example
Add the __init__() function to the Student class:
'''



class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    '''
    When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    '''
    

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    
#or

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

    #Python also has a super() function that will make the child class inherit all the methods and properties from its parent


# In[91]:



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


# In[103]:




'''
Go create a separate file mymodule.py

with content as 


def greeting(name):
  print("Hello, " + name)

'''


# In[113]:


import mymodule

mymodule.greeting("Jonathan")


# In[ ]:





# In[ ]:





# In[ ]:




