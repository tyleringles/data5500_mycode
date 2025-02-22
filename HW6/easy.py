import time  

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]  # My list of numbers for the maths

tot = 0  # This is like my box that will hold my numbers
num_elem = 0  # This will count how many numbers are in my list

start = time.time()  # starts the clock to have load time

# Loops through each number in my list
for l in lst:
    tot += l  # inreses the total by adding to it
    num_elem += 1  # adds to the count of my numbers

mean = tot / num_elem  # gets my average
end = time.time()  # stops the clock to see load time

print("Sum of elements: ", tot)  
print("Mean: ", mean)  
print("Runtime (seconds): ", end - start)  

# Big O Analysis:
# My loop go's though each iteam on the list adds them up individually before the output, this would mean that as my list grows so will my run time. 
