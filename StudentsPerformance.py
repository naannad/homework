#!/usr/bin/env python
# coding: utf-8

# ## База данных Student Performance
# 
# #### пол абитуриента, национальность, уровень образования родителей, насколько качественно пообедал абитуриент перед тестом, закончил ли абитуриент подготовительные курсы, оценка по математике, оценка по чтению, оценка по письму.

# In[27]:


import pandas as pd
import seaborn as sns


# In[21]:


student = pd.read_csv("C:\\Users\\user\\PycharmProjects\\22.09.22\\Python\\PythonTasks\\Datasets\\StudentsPerformance.csv")


# In[22]:


student


# ## Колонки слишком длинные 
# 
# ### Перименуем их в слова попроще

# In[23]:


student = student.rename(columns={
    'gender': 'sex', 
    'race/ethnicity': 'race', 
    'parental level of education': 'level', 
    'lunch': 'lunch', 
    'test preparation course': 'test', 
    'math score': 'math', 
    'reading score': 'reading', 
    'writing score':'writing'
})


# ### Проверим изменения и выведем информацию

# In[14]:


student.info()


# ## Начнем с простых вопросов
# 
# ### Сколько женщин? Сколько мужчин? 

# In[29]:


sns.countplot(x=student["sex"])


# ## Какие существуют группы?
# 
# ### По названиям 

# In[30]:


sns.countplot(x=student["race"])


# ### Сколько студентов сдали и завалили экзамен 

# In[31]:


sns.countplot(x=student["test"])


# ## Средний бал по математике (2 варианта) 
# 
# ### С другими предметами аналогично 

# In[34]:


student.math.mean()


# In[35]:


print(f"Discipline average Mathematic: {student['math'].mean()}")


# In[36]:


print(f"Discipline average Reading: {student['reading'].mean()}")


# In[37]:


print(f"Discipline average Writing: {student['writing'].mean()}")


# ## Добавим сложный вопрос
# 
# ### Сколько студентов, питающихся стандартным питанием, провалили тест?

# In[45]:


student[(student['lunch'] == 'standard') & (student['test'] == 'none')]["sex"].count()

