#assignment 2:- list1=[10,20.40,60,70,80]   list2=[5,15,25,35,45,60] merge these two sorted list product list,but used only one loop where while or for only one time ;dont used sort method

list1 = [10,20,40,60,70,80] 
list2 = [5,15,25,35,45,60] 
print ("The list 1 is : " + str(list1)) 
print ("The list 2 is : " + str(list2)) 
 
size_1 = len(list1) 
size_2 = len(list2) 
  
res = [] 
i, j = 0, 0
  
while i < size_1 and j < size_2: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i += 1
  
    else: 
      res.append(list2[j]) 
      j += 1
  
res = res + list1[i:] + list2[j:] 
  
# printing result 
print ("The mergesorted list is : " + str(res)) 
