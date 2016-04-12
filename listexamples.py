#a = 1
#b = 2

#l = [a, b, 3]
#print l
#l.append(4)
#print l 

def remove(list_, index):
    return list_[:index - 1] + list_[index:]


l = [1, 2, 3]    
print remove(l, 2)


