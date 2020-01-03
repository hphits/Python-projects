#!/usr/bin/env python
# coding: utf-8

# In[41]:


'''
The prupose of this programming challenge is to find the prime factors of a given number using object-orientated
programing. 

''' 

# Attribute of class prime

class primefactor():
    
    def __init__(self,n):
        self.prime = n
        
# Method: To check if the user input number is prime or not. 
        
    def isitprime(self):
        if self.prime <= 3:
            return True
        else:
            for i in range(2,self.prime-1):
                if self.prime % i == 0:
                    return False 
                else:
                    continue
            return True
            

# Method: find two numbers which multiply to give the user input number.
            
            
    def numfactors(self):
        factorlist = []
        for i in range(2,10):
            if self.prime % i == 0:
                d = int(self.prime / i)
                factorlist.append(i)
                factorlist.append(d)
                break
        return factorlist
    
# Method: breaking down numbers in factorlist to primenumbers
    
    def smallfactors(self,alist):
        smallfactorlist = []
        for num in alist:
            if num == 2 or num == 3:
                smallfactorlist.append(num)
                continue
            for i in range (2, num-1):
                if num % i == 0:
                    c = int(num / i)
                    d = int(i)
                    smallfactorlist.append(c)
                    smallfactorlist.append(d)
                    break
        return smallfactorlist

# Method: To check the numbers in a list if they are prime or not
                    
    def checklist(self,samplelist):
            for num in samplelist:
                if num == 2:
                    pass
                for i in range (2, num-1):
                    if num % i != 0:
                        continue
                    else: 
                        return False
            return True
        
# Method: Multiplying the numbers in the list. 
    
    def multoflist(self,alist):
        result = 1
        for i in alist:
            result = result * i
        return result
    
        
while True: 
    
    # user enters a non-prime number
    
    n = int(input('Enter a non-prime number: '))
    
    thenumber = primefactor(n)
    
    # check if the number is a prime number or not. 
    
    if thenumber.isitprime() is True:
        
        print('The number you entered is a prime number. Re-enter another number ')
        
        continue
    
    else:
        
        # find factors of the user input number
        
        h = thenumber.numfactors()
        
        # check if the factors are prime numbers or not
        
        thecheckforh = thenumber.checklist(h)
        
        if thecheckforh is True:
            
            print(h)
            
            print(f'The total of the numbers in the list {thenumber.multoflist(h)}')
            
            break
            
        # break into smaller number factors of the given number.
        
        p = thenumber.smallfactors(h)
        
        # check if the smaller number factors are prime numbers or not. If not, then the process repeats.
        
        thecheck = thenumber.checklist(p)
        
        while thecheck is False:
            
            p = thenumber.smallfactors(p)
            
            thecheck = thenumber.checklist(p)
        
        else:
            
            print(p)
        
            print(f'The total of the numbers in the list {thenumber.multoflist(p)}')
            
            break
    
    break
        


# In[ ]:




