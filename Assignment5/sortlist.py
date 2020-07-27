
#Assignment 1:- [0,1,2,10,4,1,0,56,2,0,1.3,0,56,0,4] sort increasing order but all zeros should be at right hand side 

def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)

print(move_zero([0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]))
