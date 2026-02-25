# started my leetcode on 25/2/2026

#first problem today is two sum. where the target is given and I need to add the tow arrays of intergers and return the indices of the number which fullfiled the target 

class Solution:
    def twoSum(self, nums:List[int],target:int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            numbers = nums[i]
            remaining_number = target - numbers  # need to find remaining number to fulfil target 

            if remaining_number in seen:
                return [seen[remaining_number,i]]
            
            seen[numbers]=i


#another solution which I did but had more time complexity and is not recommended is ---

class Solution:
    def twoSum(self, nums:List[int],target:int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                nums [i] + nums [j] == target
                return [i,j]