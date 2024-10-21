def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

numbers = [3, 5, 2, 9, 7, 4]
largest_number = find_largest(numbers)
print("The largest number is", largest_number)
