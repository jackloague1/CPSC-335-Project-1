def sort(lists):
    sorting = True
    total = 0
    moves = 0
    while moves > 0 or sorting:
        sorting = False
        moves = 0
        for i in range(0, len(lists)-1):
            if lists[i + 1] > lists[i]:
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
                moves += 1   
        total += moves 

        for i in range(len(lists)+1 , 0):
            if lists[i] > lists[i + 1]:
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
                moves += 1
        total += moves 

        for i in range(0, len(lists)):
            if lists[i] != 0:
                sorting == False

            else:
                 sorting == True
    new_list = [str(l) for l in lists]    
     
    print(' '.join(new_list) )
    return total

m = 0
n = 4
lists = [0, 1] * n
string_list = [str(s) for s in lists]

print("Let 0 be light and 1 be dark.")
print("The disks before sorting when n is", n,":")
print(' '.join(string_list) )
print("The disks after sorting:")
print(sort(lists))