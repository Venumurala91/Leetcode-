class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i]==target:
                return i
            
            elif nums[i]>target:
                return i
        
        if target not in nums:
            return i+1
        

        