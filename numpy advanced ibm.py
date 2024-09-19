#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
b=[4,7,8,12]
print(type(a))
print(a.shape)
print(b)
print(type(b))


# In[2]:


print(a[0],a[1],a[2])
a[0]=5
print(a)
b=np.array([[1,2,3] , [4,5,6]])
print(b.shape)
print(b[0,0] , b[0,1] , b[1,0])


# In[5]:


#numpy functions
import numpy as np
a=np.zeros((2,2))
print(a)

b=np.ones((1,2))
print(b)

c=np.full((2,2), 7)
print(c)

d=np.eye(2)
print(d)

e=np.random.random((2,2))
print(e)


# In[9]:


import numpy as np
np.linspace(2.0, 3.0, num=5, retstep=True)


# In[7]:


import numpy as np
np.linspace(2.0, 3.0, num=5)


# In[8]:


import numpy as np
np.linspace(2.0, 3.0, num=5, endpoint=False)


# In[10]:


#slicing
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3]
print(a[0,1])


# In[25]:


#slicing #f
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[-3:-1,-2:-1]
print(b)


# In[17]:


#b
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3]
print(b)


# In[18]:


#c
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[0:2,1:2]
print(b)


# In[19]:


#d
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[2:3,0:2]
print(b)


# In[20]:


#e
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:]
print(b)


# In[24]:


#g
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[-2:1,1:3]
print(b)


# In[26]:


import numpy as np
a=np.array([[1,2] , [3,4] ,[5,6]])
print(a[[0,1,2],[0,1,0]])

print(np.array([a[0,0],a[1,1],a[2,0]]))

print(a[0,0],a[1,1])

print(np.array([a[0,1],a[0,1]]))


# In[34]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array([0,2,0,1])
print(a[np.arange(4), b])
a[np.arange(4), b] += 10
print(a)


# In[38]:


#b00lean array indexing
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
bool_idx=(a>2)
print(bool_idx)
print (a[bool_idx])
print(a[a>2])


# In[45]:


#data type
import numpy as np
x=np.array([1,2])
print(x.dtype)
x=np.array([1.0,2.0])
print(x.dtype)
x=np.array([1,2],dtype=np.int64)
print(x.dtype)


# In[52]:


#array math
import numpy as np
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)
print(x+y)
print(np.add(x,y))

print(x-y)
print(np.subtract(x,y))

print(x*y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))



# In[ ]:


#transpose of array

