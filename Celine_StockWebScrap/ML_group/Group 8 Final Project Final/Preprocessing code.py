#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re


# In[2]:


filename = r'DataSet.xlsx'
open_file = pd.read_excel(filename)
in_bal = open_file[open_file['in_balanced_dataset'] == 't']
df = in_bal.drop(['in_balanced_dataset'], axis = 1) #drop balanced data


# In[3]:


#break location to country, state, city
def extract_loc(values,index):
    country = str(values).split(',')
    if len(country) == 3:
        return country [index]
    else:
        return country[0] 


# In[4]:


#plot graph
df['country'] = df['location'].apply(lambda x:extract_loc(x,0))
df['country'].value_counts().plot.bar() 
plt.show()
df['state'] = df['location'].apply(lambda x:extract_loc(x,1))
df['state'].value_counts().plot.bar()
plt.show()
df['city'] = df['location'].apply(lambda x:extract_loc(x,2))
df['city'].value_counts().plot.bar()
plt.show()
#remove "location" column
df.drop('location', axis=1, inplace= True)


# In[5]:


#all char used in title
char_set = set(df.title.apply(list).sum())
print(char_set)


# In[6]:


#find percentage of capslock on title
def countcaps(values):
    countc = re.findall(r'[A-Z]', str(values)) #find capslock character
    countl = re.findall(r'[a-z]', str(values)) #find lower case char
    return len(countc)/(len(countc)+len(countl)) #count capslock char percentage

df['title_caps'] = df['title'].apply(lambda x: countcaps(x))


# In[7]:


#employment type graph
df['employment_type'].apply(lambda x : str(x)).value_counts().plot.bar()
plt.show()

#required experience graph
df['required_experience'].apply(lambda x: str(x)).value_counts().plot.bar()
plt.show()

#required education graph
df['required_education'].apply(lambda x: str(x)).value_counts().plot.bar()
plt.show()

#function graph
df['function'].apply(lambda x: str(x)).value_counts().plot.bar()
plt.show()

#industry involved graph
df['industry'].apply(lambda x: str(x)).value_counts().plot.bar()
plt.show()


# In[8]:


#description feature
def count (values, char):
    count =re.findall(r'{0}'.format(char), str(values))
    if len(count) > 0:
        return np.log10(len(count) +1)
    else:
        return 0


# In[9]:


#x-axis:log_num, y-axis: amount
#data range 0-1
#bullet count for each feature
df['description_bul_cnt_norm'] = df['description'].apply(lambda x: count(x,'<li>')).apply(lambda x: min(x / 2.0, 1.0))
df['description'].apply(lambda x: count(x,'<li>')).hist(bins=25) 
plt.show()
df['company_profile_bul_cnt_norm']=df['company_profile'].apply(lambda x: count(x,'<li>')).apply(lambda x: min(x / 2.0, 1.0))
df['company_profile'].apply(lambda x: count(x,'<li>')).hist(bins=25)
plt.show()
df['requirements_bul_cnt_norm'] = df['requirements'].apply(lambda x: count(x,'<li>')).apply(lambda x: min(x / 2.0, 1.0))
df['requirements'].apply(lambda x: count(x,'<li>')).hist(bins=25)
plt.show()
df['benefits_bul_cnt_norm']= df['benefits'].apply(lambda x: count(x,'<li>')).apply(lambda x: min(x / 2.0, 1.0))
df['benefits'].apply(lambda x: count(x,'<li>')).hist(bins=25)
plt.show()

#paragraph count
df['description_par_cnt_norm'] = df['description'].apply(lambda x: count(x,'<p>')).apply(lambda x: min(x / 2.0, 1.0))
df['description'].apply(lambda x: count(x,'<p>')).hist(bins=25)
plt.show()
df['company_profile_par_cnt_norm'] = df['company_profile'].apply(lambda x: count(x,'<p>')).apply(lambda x: min(x / 2.0, 1.0))
df['company_profile'].apply(lambda x: count(x,'<p>')).hist(bins=25)
plt.show()
df['requirements_par_cnt_norm'] = df['requirements'].apply(lambda x: count(x,'<p>')).apply(lambda x: min(x / 2.0, 1.0))
df['requirements'].apply(lambda x: count(x,'<p>')).hist(bins=25)
plt.show()
df['benefits_par_cnt_norm']= df['benefits'].apply(lambda x: count(x,'<p>')).apply(lambda x: min(x / 2.0, 1.0))
df['benefits'].apply(lambda x: count(x,'<p>')).hist(bins=25)
plt.show()

#bold count
df['description_bold_cnt_norm'] = df['description'].apply(lambda x: count(x,'<b>')).apply(lambda x: min(x / 2.0, 1.0))
df['description'].apply(lambda x: count(x,'<b>')).hist(bins=25)
plt.show()
df['company_profile_bold_cnt_norm'] = df['company_profile'].apply(lambda x: count(x,'<b>')).apply(lambda x: min(x / 2.0, 1.0))
df['company_profile'].apply(lambda x: count(x,'<b>')).hist(bins=25)
plt.show()
df['requirements_bold_cnt_norm'] = df['requirements'].apply(lambda x: count(x,'<b>')).apply(lambda x: min(x / 2.0, 1.0))
df['requirements'].apply(lambda x: count(x,'<b>')).hist(bins=25)
plt.show()
df['benefits_bold_cnt_norm']= df['benefits'].apply(lambda x: count(x,'<b>')).apply(lambda x: min(x / 2.0, 1.0))
df['benefits'].apply(lambda x: count(x,'<b>')).hist(bins=25)
plt.show()


# In[10]:


#for url, phone, email
#replace text to avoid complexity
def dropsha2 (values, prefix):
    find = re.findall(r'#{0}'.format(prefix),str(values))
    if len(find) > 0: 
        replace = re.sub(r"#" + prefix + "_[A-Za-z0-9]{10,128}#", "^" + prefix + "^", str(values))
        return replace
    else:
        return values


# In[11]:


#URL
df['description'] = df['description'].apply(lambda x: dropsha2(x , 'URL'))
df['company_profile'] = df['company_profile'].apply(lambda x: dropsha2(x , 'URL'))
df['requirements'] = df['requirements'].apply(lambda x: dropsha2(x , 'URL'))
df['benefits'] = df['benefits'].apply(lambda x: dropsha2(x , 'URL'))

#PHONE
df['description'] = df['description'].apply(lambda x: dropsha2(x , 'PHONE'))
df['company_profile'] = df['company_profile'].apply(lambda x: dropsha2(x , 'PHONE'))
df['requirements'] = df['requirements'].apply(lambda x: dropsha2(x , 'PHONE'))
df['benefits'] = df['benefits'].apply(lambda x: dropsha2(x , 'PHONE'))

#Email
df['description'] = df['description'].apply(lambda x: dropsha2(x , 'EMAIL'))
df['company_profile'] = df['company_profile'].apply(lambda x: dropsha2(x,'EMAIL'))
df['requirements'] = df['requirements'].apply(lambda x: dropsha2(x , 'EMAIL'))
df['benefits'] = df['benefits'].apply(lambda x: dropsha2(x , 'EMAIL'))


# In[12]:


#URL count
df['description_url_cnt_norm'] = df['description'].apply(lambda x: count(x,'\^URL\^')).apply(lambda x: min(x / 2.0, 1.0))
df['description'].apply(lambda x: count(x,'\^URL\^')).hist(bins=25)
plt.show()
df['company_profile_url_cnt_norm'] = df['company_profile'].apply(lambda x: count(x,'\^URL\^')).apply(lambda x: min(x / 2.0, 1.0))
df['company_profile'].apply(lambda x: count(x,'\^URL\^')).hist(bins=25)
plt.show()
df['requirements_url_cnt_norm'] = df['requirements'].apply(lambda x: count(x,'\^URL\^')).apply(lambda x: min(x / 2.0, 1.0))
df['requirements'].apply(lambda x: count(x,'\^URL\^')).hist(bins=25)
plt.show()
df['benefits_bold_url_norm'] = df['benefits'].apply(lambda x: count(x,'\^URL\^')).apply(lambda x: min(x / 2.0, 1.0))
df['benefits'].apply(lambda x: count(x,'\^URL\^')).hist(bins=25)
plt.show()


# In[13]:


#for telecommuting, company logo, questions, fraudulent (binary result)
#count total f and t
def count (values):
    if str(values) == 't':
        return True
    elif str(values) == 'nan' : #find if datas have blank value
        return 'Nan'
    else:
        return False


# In[14]:


#telecommuting
df['telecommuting'].apply(lambda x: count(x)).value_counts().plot.bar()
plt.show()

#company logo
df['has_company_logo'].apply(lambda x: count(x)).value_counts().plot.bar()
plt.show()

#questions
df['has_questions'].apply(lambda x: count(x)).value_counts().plot.bar()
plt.show()

#fraudulent
df['fraudulent'].apply(lambda x: count(x)).value_counts().plot.bar()
plt.show()


# In[15]:


#update data 
# Eloff 2019: https://stackoverflow.com/a/925630 
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    if isinstance(html, str):
        s = MLStripper()
        s.feed(html)
        return s.get_data().replace(u'\xa0', u' ') # remove non breaking space
    else:
        return html

df['description'] = df['description'].apply(lambda x: strip_tags(x))
df['company_profile'] = df['company_profile'].apply(lambda x: strip_tags(x))
df['requirements'] = df['requirements'].apply(lambda x: strip_tags(x))
df['benefits'] = df['benefits'].apply(lambda x: strip_tags(x))


# In[16]:


#convert new data to excel
file_name = 'Newdata1.xlsx'

# saving the excelsheet
df.to_excel(file_name)
print('Successfully exported into Excel File')

