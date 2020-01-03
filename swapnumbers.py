#!/usr/bin/env python
# coding: utf-8

# In[31]:


def maxvalue(n):
    
    n = str(n)
    nlist = []
    
    for i in n:
        nlist.append(i)
    
    for i in range(0,len(nlist)):
        for p in range(i,len(nlist)):
            if nlist[i] > nlist[p]:
                continue
            elif nlist[i] < nlist[p]:
                a = nlist[i]
                nlist[i] = nlist[p]
                nlist[p] = a
                break
        break
    
    finalnumber = "".join(nlist)
    finalnumber = int(finalnumber)
    
    if int(n) == finalnumber:
        print("No swap")
        return n
    else:
        print(f"Swap the number {a} and the number {nlist[i]}.")
        return finalnumber
    
    
    


# In[34]:


maxvalue(1120)


# In[ ]:




