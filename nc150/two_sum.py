
def twoSum( nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]!=nums[j] and nums[i]+nums[j] == target:
                return type([i, j])
                
arr = [3,4,5,6] 
target = 7
a = twoSum(arr, target)
print(a)