# Function that contains the sorting algorithm that will sort the list of disks.
def sort(n, lists):
    sorting = False # Determines whether the list is sorted.
    m = 0           # Total swaps taken to sort the list.
    moves = 0       # Total swaps taken during one iteration of the while loop.

    # Iterate through while loop until the list is sorted or no more swaps are needed.
    while moves > 0 or sorting == False:
        moves = 0

        # Iterating through the list from left to right.
        for i in range(0, len(lists)-1):
            if lists[i + 1] == "dark" and lists[i] == "light":
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
                moves += 1

        # Iterating through the list from right to left.
        for i in range(len(lists)+1, 0):
            if lists[i] == "dark" and lists[i - 1] == "light":
                temp = lists[i]
                lists[i] = lists[i - 1]
                lists[i - 1] = temp
                moves += 1

        # Computes total swaps taken to sort the list.
        m += moves

        # Checking if the list is sorted by checking if the first n elements are all dark.
        for i in range(0, n):
            if lists[i] != "dark":
                sorting = False
                break
            else:
                 sorting = True   
    
    # Outputs the sorted list of disks (with all darks on the left side and all lights on the right side).
    print(' '.join(lists))
    # Outputs the number of swaps performed to sort the list.
    print("\nThe number of swaps taken:")
    return m

# Asking user to enter a number to represent the amount of light and dark disks.
input_n = input("Please enter a positive integer n for the amount of n light and n dark disks: ")

# Checking if the input is a positive integer.
if input_n.strip().isdigit() and int(input_n) > 0:
    n = int(input_n)
    # Creates a list of 2n alternating strings with "light" representing light disks and "dark" representing dark disks.
    lists = ["light", "dark"] * n
    string_list = [str(s) for s in lists]
    print("Let the string 'light' represent light disks and 'dark' represent dark disks.\n")
    print("The disks before sorting when n is", n,":")
    print(' '.join(string_list) )
    print("\nThe disks will be sorted with dark disks on the left side and light disks on the right side.")
    print("\nThe disks after sorting:")
    print(sort(n, lists))
    
# Ends program if the input is not a positive integer. 
else:
    print("The input is not a positive integer. Please rerun the program and try again.")
