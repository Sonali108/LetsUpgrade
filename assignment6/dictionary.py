#Assignment6
#Que 1:- list1=[1,2,3,4,5,7,8] list2=["a","b","c","d","e"]conver to a directory.in one line code using list comprehension(without using zip method)
list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]
list=[(k,v) for k in list1 for v in list2 if list1.index(k)==list2.index(v)]
print("Required dictonary of above two list is\n",dict(list))
