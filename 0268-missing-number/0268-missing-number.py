class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # if 0 not in nums:
        #     return "0"

        summ=sum(nums)
        nums_summ=0
        for i in range(len(nums)+1):
            nums_summ+=i


        
        return nums_summ-summ

        


    