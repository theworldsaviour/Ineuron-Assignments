#!/usr/bin/env python
# coding: utf-8

# In[6]:


#check if no is positive, negative or zero
a=int(input("Enter the Number: "))
if (a >0):
    print("{} is a positive number".format(a))
elif (a==0):
    print("Number is 0")
else:
    print("{} is a negative number".format(a))


# In[13]:


#check if no is odd or even
b=int(input("Enter the Number: "))
if (b %2 == 1):
    print("{} is a odd number".format(b))
elif(b==0):
    print("0 is neither odd nor even")
else:
    print("{} is a even number".format(b))


# In[16]:


#check if no is odd or even
yy=int(input("Enter the Year: "))
if(yy>0):
    if (yy %4 == 0):
        print("{} is a leap Year".format(yy))
    
    else:
        print("{} is a non leap year".format(yy))
else:
    print("Please enter correct Year")


# In[22]:


#Check Prime Number
p = int(input("Enter the number: "))
if (p==0 or p==1):
    print("{} is neither prime nor co-prime")
else:
    for i in range(2,p):
        if(p%i==0):
            print(p, "is not a prime number")
            break
    else:
        print(p, "is a prime number")


# In[48]:


#Print Prime Number between 1 - 10000
for g in range(2,10001):
    for i in range (2, g):
            if(g%i==0):
                break            
    else:
        print(g)


# In[ ]:




