#!/usr/bin/env python
# coding: utf-8

# In[18]:


#BMI Calculator 
name= input ("Enter Your Name:")
Weight= int(input ("Enter Your Weight in Pounds:") )
Height= int(input ("Enter Your Height in Inches:") )
BMI= (Weight*703)/(Height*Height)
print("Your BMI is:", BMI)
#Conditions
if BMI>0:
    if(BMI<18.5):
        print(name +", you are underwight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")
    
    


# In[ ]:





# In[ ]:




