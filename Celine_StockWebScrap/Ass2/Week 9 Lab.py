#!/usr/bin/env python
# coding: utf-8

# In[13]:


#1
counts = dict()
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        day = line[2]
        counts[day] = counts.get(day,0)+1
dow = ('Thu', 'Fri', 'Sat')
for day in dow:
    print(day, counts[day])


# In[14]:


#2
counts = dict()
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        hour = time.split(':')[0]
        counts[hour]= counts.get(hour,0)+1
for k,v in sorted(counts.items()):
    print(k,v)


# In[12]:


#3-1
counts = dict()
fhand = open('mbox-large.txt')
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        day = line[2]
        counts[day] = counts.get(day,0)+1
dow = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
for day in dow:
    print(day, counts[day])


# In[15]:


#3-2
counts = dict()
fhand = open('mbox-large.txt')
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        hour = time.split(':')[0]
        counts[hour]= counts.get(hour,0)+1
for k,v in sorted(counts.items()):
    print(k,v)


# In[16]:


#4
counts = dict()
fhand = open('briefing0326.txt', encoding='utf-8')
for line in fhand:
    if line.startswith('无症状感染者'):
        line = line.split('，')
        dname = line[3][3:]
        counts[dname] = counts.get(dname,0)+1
for k,v in sorted(counts.items(), reverse=True, key=lambda x:x[1]):
    print(k,v)


# In[ ]:




