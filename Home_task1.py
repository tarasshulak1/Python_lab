import random


########## create list of 100 random numbers from 0 to 1000 ##########
numbers = random.sample(range(1001), 100)



########### sort list from min to max (without using sort()) ##########

# create new list for storing sorted values
sorted_list = []

# copy into separate list. Original list is not modified
nums = numbers[:]

while nums:
    # assuming that first value in the list is the smallest
    minimum = nums[0]
    # go through the copied list
    for x in nums:
        # check each value in the list if it less than our assumed minimal value
        if x < minimum:
            # If we find a smaller number, we update minimum
            minimum = x
    # add the minimal value to the new sorted_list
    sorted_list.append(minimum)
    # remove this minimal value from the copied list in order to check others values and omit duplicates
    nums.remove(minimum)



########## calculate average for even and odd numbers ##########

# find sum of even number
even_total_sum = 0
even_count = 0
for item in numbers:
    if item % 2 == 0:
        even_total_sum += item
        even_count += 1

# find sum of odd number
odd_total_sum = 0
odd_count = 0
for item in numbers:
    if item % 2 != 0:
        odd_total_sum += item
        odd_count += 1

# calculate avg for even
even_avg = even_total_sum/even_count
odd_avg = odd_total_sum/odd_count

print(even_avg)
print(odd_avg)







