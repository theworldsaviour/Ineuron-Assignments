#!/usr/bin/env python
# coding: utf-8

# In[3]:


#kilometers to Miles
a=int(input("Enter the Value in KM: "))
b=a/1.6
print("{} KM is equivalent to {} miles".format(a,b))


# In[4]:


#Celsius to Fahrenheit
c=float(input("Enter the temp in Celcius: "))
d= (c*9/5)+32
print("{} celcius is equal to {} Farenhite".format(c,d))


# In[5]:


#display Calendar
import calendar

Year = int(input("Enter the year: "))
Month = int(input("Enter the month: "))

print(calendar.month(Year, Month))


# In[7]:


#quadratic equation
import cmath
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d= (b**2)-(4*a*c)
EQ1 = (-b-cmath.sqrt(d))/(2*a)
EQ2 = (-b+cmath.sqrt(d))/(2*a)

print("the Solution for quadratic equation is{} & {} ".format(EQ1 , EQ2) )


# In[11]:


#swap 2 variables without temp
x = 77
y =55

x=x+y
y=x-y
x=x-y
print(x,y)


# In[ ]:




