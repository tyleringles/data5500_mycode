import time  

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]  # my lis of numbers

# Finding the  MAX
def max_difference(arr):
    if len(arr) < 2:  
        return None  

    min_val = min(arr)  # finds the smallest # (not a hashtag)
    max_val = max(arr)  # finds the largest # (not a hashtag)

    return max_val - min_val  # subtracts the smallest from the largest

start = time.time()  # Start the clock

max_diff = max_difference(lst)  #finds differnce between the two

end = time.time()  # End the timer to see how long the code took

print("Maximum difference: ", max_diff)  
print("Runtime (seconds): ", end - start)  

# Big O Complexity Analysis:
#functions look at every number in the list to find the smallest and biggest numbers. Each one takes the same amount of time, depending on how many numbers there are. Since they do this one after the other, the time it takes is still based on how many numbers are in the list, make each questions runtime rely on the size of their list. 
print("Thanks pal")  # thanking my code 
