#!/usr/bin/env python
# coding: utf-8

# In[6]:


#print Hello Python
print("Hello Python")


# In[27]:


#Program to fo addition & division
a,b = 10,5
c=a/b
d=a+b
print(c)
print(d)


# In[30]:


#Program for area of a triangle
a1=float(input("Enter the first side dimension"))
a2=float(input("Enter the second side dimension"))
a3=float(input("Enter the third side dimension"))
s = (a1+a2+a3)/2

Area = (s*(s-a1)*(s-a2)*(s-a3)) **0.5
print("{} is the area of triangle ".format( Area))


# In[29]:


#Swap 2 variables
d= int(input("Enter the First no for A: "))
e= int(input("Enter the Second no for B: "))

temp =d
d = e
e=temp

print("The value of A after swap is: {} ".format(d) )
print("The value of B after swap is: {} ".format(e) )


# In[34]:


#Generate Random No
import random
print(random.randrange(1,20))


# In[ ]:





# In[ ]:




