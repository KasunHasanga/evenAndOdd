





def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=(12,13,14,15,16,18,27,2,85)


even,odd=count(lst)

print("even= {} and odd = {}" .format(even,odd))