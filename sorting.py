def sort(lists):
    sorting = True
    m = 0
    moves = 0
    while moves > 0 or sorting:
        sorting = False
        moves = 0
        # Iterating through the list from left to right.
        for i in range(0, len(lists)-1):
            if lists[i + 1] == "dark" and lists[i] == "light":
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
                moves += 1   
        #m += moves
        # Iterating through the list from right to left.
        for i in range(len(lists)+1 , 0):
            if lists[i] == "dark" and lists[i - 1] == "light":
                temp = lists[i]
                lists[i] = lists[i - 1]
                lists[i - 1] = temp
                moves += 1
        m += moves
        # Checking if the list is sorted.
        for i in range(0, len(lists)):
            if lists[i] != "light":
                sorting == False

            else:
                 sorting == True
    # Converting list of integers to strings to make it look better.           
    new_list = [str(l) for l in lists]    
    
    print(' '.join(new_list) )
    print("The number of swaps taken:")
    return m

# Initializing list of disk.
input_n = input("Please enter a positive integer n for the amount of n light and n dark disks: ")
# Checking if the input is a positive integer.
if input_n.strip().isdigit():
    n = int(input_n)
    lists = ["light", "dark"] * n
    string_list = [str(s) for s in lists]
    print("Let 0 be light and 1 be dark.")
    print("The disks before sorting when n is", n,":")
    print(' '.join(string_list) )
    print("The disks after sorting:")
    print(sort(lists))
    
# Ends program if the input is not a positive integer. 
else:
    print("The input is not a positive integer. Please try again.")
