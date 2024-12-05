class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c={}
        for i in range(len(nums)):
            c[nums[i]]=c.get(nums[i],0)+1


        for key,value in c.items():
            if value==1:
                return key 

        