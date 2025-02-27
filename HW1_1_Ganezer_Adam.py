#!/usr/bin/env python
# coding: utf-8

# ### Write your full name and Perm number below

# Full name: Ganezer, Adam
# 
# Perm number: A1H8141
# 
# Change the filename to HW1_1 followed by your last name and first name with an underscore between them. For example, Abraham Lincoln's homework filename would be "HW1_1_Lincoln_Abraham.ipynb"

# ### **Homework 1_1**
# 
# The goal is to generate two random DNA sequences and compare them.
# 
# Please read the insturctions and comments in cells, and follow them carefully.
# 
# ---
# 

# #### Dice() function
# 
# The following cell defines a function, dice(), that you will use in the homework. You do not need to know how to define a function, which will a subject of the 2nd week. For now, it is enough to know that you will use it in the homework.
# 
# 
# The function dice() will randomly generate an integer number whenever you call it.
# The range of the generated random number is from 1 to 4.
# 
# Run the cell so that the function can be used in the following cells.

# In[16]:


from random import seed
from random import random
from time import time
from math import ceil
seed(time())
def dice():
    a = ceil(random()*4)
    if a>0:
        return a
    else:
        return dice()


# Here is how to use the function dice().

# In[17]:


n = dice()
print(n)


# ### **IMPORTANT**
# A line starting with `def` defines a function. When you code your answer to the following questions, you will write it inside the function definition. This helps the TA to check your answers easily. 
# 
# Remember that all lines must be indented properly.
# 
# ---

# #### **Problem 1 (0.5 pt)**
# 
# Write code to generate 100 random numbers ranging from 1 to 4 using the function dice(), and print them. Hint: Use a 'for' loop.
# 
# Confirm that it indeed generates a random integer bewteen or equal to 1 and 4
# 
# The output should look like below:
# 
# ![HW1_1_prob1_result_1.png](attachment:6c6a4ebd-d811-4d72-a74c-8f870d0a6dc8.png)
# ...
# ![HW1_1_prob1_result_2.png](attachment:45c8cd33-d56d-4d4d-828a-13c25c71cbfb.png)

# In[ ]:


def Prob1():
    # Complete the code below
    for n in range(100):
        n= dice()
        print(n)


# In[ ]:


# When you run this code, the result should look the same as the expected outcome.
Prob1()


# #### **Problem 2 (1.5 pt)**
# Write code that counts the occurrance of each number while you run dice() 100 times. Then print the occurrance of each number. For example, the example output would look like below. Note that the actual number may vary in every simulation: <br>
#     &emsp; Number 1 occurred 22 times <br>
#     &emsp; Number 2 occurred 30 times <br>
#     &emsp; Number 3 occurred 27 times <br>
#     &emsp; Number 4 occurred 21 times <br>
#     
# Hint 1: Use a variable for each number to count the ocurrence while generating the random integers.<br>
# Hint 2: Use a IF/ELIF/ELSE statement.

# In[ ]:


def Prob2():
    n1=0
    n2=0
    n3=0
    n4=0
    # Complete the code below
    for n in range(100):
        n= dice()
        if n==1:
            n1+=1
        elif n==2:
            n2+=1
        elif n==3:
            n3+=1
        elif n==4:
            n4+=1
    print ("Number 1 occurred", (n1), "times")
    print ("Number 2 occurred", (n2), "times")
    print ("Number 3 occurred", (n3), "times")
    print ('Number 4 occurred', (n4), "times")


# In[ ]:


# When you run this code, the result should look the same as the expected outcome.
Prob2()


# #### **Problem 3 (1.5 pt)**
# Write code performing:
# 1. Generate a random number using dice()
# 2. Print a string using the following map
#     - If the generated number is 1, print '1 A'
#     - If the generated number is 2, print '2 T'
#     - If the generated number is 3, print '3 C'
#     - If the generated number is 4, print '4 G'
#     
# Hint: Use a IF/ELIF/ELSE statement.
# 
# The outcome will look like this (actual number should vary in each simulation):
# ![HW1_1_prob3_result.png](attachment:ad213380-b35e-46af-b861-dcee3920bb79.png)

# In[ ]:


def Prob3():
    a = dice()
    if a==1:      # complete the code
            print ('1 A')
    elif a==2:
            print('2 G')
    elif a==3:
            print('3 C')
    elif a==4:
            print('4 G')


# In[ ]:


# When you run this code, the result should look the same as the expected outcome.
Prob3()


# #### **Problem 4 (2 pt)**
# In this problem, we will generate a string with a length of 500. Run the dice() 500 time. For each run, convert the integer to one of ATCG using the map in Problem 3. Assign this string to a variable named "seq". Then print "seq".
# 
# Hint: Strings can be concatenated using '+' operator. For example:
# ```
# s = 'G'
# s += 'T'
# ```
# 
# The output should look like below:
# ![HW1_1_prob4_result.png](attachment:d9f72f33-0e45-4637-be79-2309e3a0dbb7.png)

# In[27]:


def Prob4():
    # Write your code here
    seq = ""
    for a in range(500):
        a = dice()
        if a==1:
            seq += 'A'
        elif a==2:
            seq += 'G'
        elif a==3:
            seq +='C'
        elif a==4:
            seq +='T'
        



    return seq


# In[33]:


# When you run this code, the result should look the same as the expected outcome.
seq = Prob4()
print(seq)


# ---
# <br>
# A letter in a string sequence can be individually accessible using index. For example, the first letter of the string variable "seq" can be accessed by "seq[0]" and the 500th letter can be accessed by "seq[499]". (In Python, the index of a string begins from 0. This may be different in other programming laguages such as Matlab, in which index begins from 1.)<br><br>
# &emsp; To access a few consecutive letters in the string, you can use ':' to indicate the range. For example, "seq[2:5]" represents the three letters from 3rd position (index 2) to 5th position (index 4). Note that the index 5 is not included, as in "range(2,5)" function. <br>
# 
# #### **Problem 5 (2 pt)**
# Count the number of occurrence of a three-letter sequence 'ACT' in the "seq" generated in Problem 4. You must use a variable name "count_ACT". Print "count_ACT".
# <br><br>
# Hint 1: Use a FOR loop to access three-letter sequences from 1st postion to 498th position. There are total 498 possible sequences. <br>
# Hint 2: In each iteration, read the three-letter sequence at each position and compare it to 'ACT' using a comparison operator.

# In[29]:


def Prob5():
    # Write your code here
    count_ACT = 0;
    for num in range(0, 497): # complete the code
        if seq [num:num+3]=="ACT":
            count_ACT+=1
    print ("Number of ACT is",count_ACT)


# In[34]:


# When you run this code, the result should print the number of occurrence of "ACT" in the sequence.
Prob5()


# #### **Problem 6 (2.5 pt)**
# 
# Compare two sequences and count the number of positions where two sequences have the same letter. To this end, generate two sequences using Problem 4. You must use variable names "seq1" and "seq2" for these two sequences. The name of the counting variable should be "count_same_pos".

# In[37]:


def Prob6():
    seq1= ""
    for a in range(500):
        a = dice()
        if a==1:
            seq1 += 'A'
        elif a==2:
            seq1 += 'G'
        elif a==3:
            seq1 +='C'
        elif a==4:
            seq1 +='T'
        


    seq2 = ""
    for a in range(500):
        a = dice()
        if a==1:
            seq2 += 'A'
        elif a==2:
            seq2 += 'G'
        elif a==3:
            seq2 +='C'
        elif a==4:
            seq2 +='T'
    count_same_pos=0
    for num in range (0,499):
        if seq1[num]==seq2[num]:
            count_same_pos+=1
    print ("Number of matched bases is",count_same_pos)
       
    
    # Write your code here


# In[38]:


# When you run this code, the result should print the number.
Prob6()


# In[ ]:





# ---
# ## **Check your code before you commit and push your homework**
# 
# ### If there is any error in your code, including any practice code you wrote to test your answers, your homework will not be scored.
# 
# #### Here are steps you must take to make sure there is no error in your script.
# 1. You must first restart the kernel. It is in the menu "kernel->Restart Kernel". Or click the restart button.
# ![restart_kernel.png](attachment:restart_kernel.png)
# 2. Run all cells. You can do this by clicking the menu "Run->Run all cells".
# 3. Fix any errors.
# 4. Repeate 1-3 until you don't see any errors.
# 5. **IMPORTNAT: Clear All Outputs (Right mouse click->Clear All Output)**
# 6. **IMPORTNAT: Save your file and change the filename to "HWn_Lastname_Firstname.ipynb"**
# 7. **Run the following cell and make sure you don't see any errors. This is the code that the TA or the instructor will use to generate testable code.**

# In[ ]:


# If the name of the student is Abraham Lincoln, then the code should look
# like below.

get_ipython().system("jupyter nbconvert --to script 'HW1_1_Ganezer_Adam.ipynb' # Change this to your name (name of this file)")
import HW1_1_Ganezer_Adam as hw  # Change this to your name
dir(hw)

# After running this code, you should see, at the bottom, the function names
# of your homework answers.

# If you see errors, please make sure the file names, module names are all
# properly set up. Then restart the kernel and try it again.


# In[ ]:





# In[ ]:




