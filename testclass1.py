#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal:
    """simple attempt to model a dog"""
    
    def __init__(self,animaltype,name,age):
        self.animaltype=animaltype
        self.name=name
        self.age=age
        print('executed and called out')
        
    def sit(self):
        """stimulate a dog sitting in resonse to a command"""
        print(f" {self.animaltype} {self.name} is sitting now")
        
    def roll(self):
        """stimulate a dog roll over in resonse to a command"""
        print(f" {self.animaltype} {self.name} rolled over!")  


# In[2]:





# In[ ]:




