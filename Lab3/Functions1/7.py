def has_33(nums):

    for i  in nums:
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
        
list = [1, 3, 3]

print(has_33(list))