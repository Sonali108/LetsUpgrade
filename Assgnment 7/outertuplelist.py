#Que3: take a list shown in below [(1,2,3),(1,2),['a','hit','less']]the list contain touple and list.make the element of inner list and tuple to outer list

list2 = [(1,2,3), [1,2], ['a','hit','less']] 
# using list comprehension 

out = [item for t in list2 for item in t]
print(out) 
