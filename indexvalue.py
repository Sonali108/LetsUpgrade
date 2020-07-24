str="what we think we become;we are python programmers" 
id1=str.index("we")
id2=str.index ("we",id1+1)
id3=str.index ("we",id2+1)
print("All the occurrences of substring 'we' are ")
print(id1,"\n",id2,"\n",id3)

