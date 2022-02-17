def sort(list):
    sorting = True
    total = 0
    moves = 0
    while moves > 0 or sorting:
        sorting = False
        moves = 0
        for i in range(0, len(list)-1):
            if list[i + 1] > list[i]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                moves += 1   
        total += moves 

        for i in range(len(list)+1 , 0):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                moves += 1
        total += moves 

        for i in range(0, len(list)):
            if list[i] != 0:
                sorting == False

            else:
                 sorting == True
                 
    print(list)
    return total

m = 0
n = 4
list = [0, 1] * n
dark = int(1)
print("Let 0 be light and 1 be dark.")
print("The list before sorting when n is", n,":")
print(list)
print("The list after sorting:")
print(sort(list))