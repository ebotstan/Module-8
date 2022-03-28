#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1
# Ask for an exam score and store that number. If the number is greater than 100, then print out 'You cannot have an exam score higher than 100'. If the number doesn't exceeed 100 but is greater than or equal to 75, then print out 'You did great on your exam!'. Otherwise if they scored lower than 75, then print out 'You need to study harder'.

# In[2]:


score = int(input("Enter your exam score: "))
if score > 100 :
    print("You cannot have an exam score higher than 100.")
elif score >= 75 :
    print("You did great on your exam")
else :
    print("You need to study harder")


# In[ ]:





# ### Exercise 2
# Ask a user to enter two numbers and find their average. Then, print out the average and whether each number is below or above average. Determine if a function should be created or not.
#     

# In[15]:


def numb_avg(numb, avg) :
    if numb < avg :
        print(f"{numb} is below the average")
    elif arg1 > avg :    
        print(f"{numb} is above the average")   
    else :    
        print(f"{numb} is equals to the average")    
    return    


# In[16]:


numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

avg = (numb1 + numb2) / 2
print(f"The average of {numb1} and {numb2} is {avg}.")

average(numb1, avg)
average(numb2, avg)


# In[ ]:





# ### Exercise 3
# Write a function to convert a test score to a grade where  
#  - 90 - 100: A
#  - 80 - 89:  B
#  - 70 - 79:  C
#  - 60 - 69:  D
#  - < 60   :  F
#  
# If a score is not between 0 and 100 then print out an error message. In the program, ask the user for a score and then call your function. 

# In[21]:


def score_grade(score) :
    if score > 100 or score < 0 :
        print("Score must be between 0 and 100.")
    elif score >= 90 :
        msg = "Grade is A"
    elif score >= 80 :
        msg = "Grade is B"
    elif score >= 70 :
        msg = "Grade is C"
    elif score >= 60 :
        msg = "Grade is D"
    else :
        msg = "Grade is F"
        
    return msg


# In[22]:


score = int(input("Please enter a test score: "))    
print(score_grade(score)) 


# In[23]:


score = int(input("Please enter a test score: "))    
print(score_grade(score)) 


# In[25]:


score = int(input("Please enter a test score: "))    
print(score_grade(score)) 


# ### Exercise 4
# Convert following decimal number to a binary number by hand:
# 
#     61
#     15
#     71
#     

# In[ ]:


""" 61 = 00111101
    15 = 00001111
    71 = 01000111
    """


# In[ ]:





# ### Exercise 5
# When a = 61 and b = 15, what is the result of following bitwise opertion? Use inline comments to show your result in a binary number. Find your answer by hand.
# 
#     a & b
#     a | b
#     a ^ b
#     a >> 2
#     

# In[ ]:


a = 61     # 0011 1101
b = 15     # 0000 1111

a & b      # 0000 1101


# In[ ]:


a | b      # 0011 1111


# In[ ]:


a ^ b      # 0011 0010


# In[ ]:


a >> 2     # 0000 1111 


# In[ ]:




