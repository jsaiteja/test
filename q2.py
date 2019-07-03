def Sort_Tuple(tup):

    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup
final_list = []
line = input("Enter the list of tuples:\n")
while(line != ''):
	final_list.append(tuple(line.split()))
	line = input()
tup= tuple(final_list)
print(Sort_Tuple(tup))
