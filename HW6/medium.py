import time

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]  # my list of numbers

# O(n) example for finding the second largest number
def second_largest(arr):
#asked chat how to referance a less than 2 numbers and to expain as if a child, then helped me create "if len(arr) <2:"
    if len(arr) < 2:  
        return None  # asked chat why it's didn't work relized my "None" was lowercaesd "none"

    first = second = float('-inf')  # Start with very small numbers for first and second largest

    # Loop through each individual number on the list
    for num in arr:
        if num > first:  # If functionhelps order the number correctily on size
            second = first
            first = num 
        elif num > second and num != first:  # If functionhelps order the number correctily on size but for the second number
            second = num  # corrects/updates number

    return second  # Return the second largest number

start = time.time()  # Start the clock to get time

second_largest_num = second_largest(lst)  # shows 2 largest number

end = time.time()  # Ends clock to recive the time


print("Second largest number: ", second_largest_num)  
print("Runtime (seconds): ", end - start)  

# Big O Complexity Analysis:
# Like the easy problem it gos though each iteam on the list indiviually doing the commparission one by one, however it is consitant. But adding to the list will add more run time on th clock. This also had more consitant runtime than problem one where it would flucute by 1-1.5 seconds.