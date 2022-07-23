# write main code here 
list_1_to_1000 = [x for x in range(0,1001)]
EVEN_LIST = []
ODD_LIST  = []
for element in list_1_to_1000 :
    if element%2 == 0 :
        EVEN_LIST.append(element)
    else:
        ODD_LIST.append(element)

# printing list in reverse odrer 
EVEN_LIST.sort(reverse=True)
ODD_LIST.sort(reverse=True)

print(tuple(EVEN_LIST))
print(tuple(ODD_LIST))
