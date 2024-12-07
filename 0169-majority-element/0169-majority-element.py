class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1

        
        for key,value in dic.items():
            if value > len(nums)//2:
                return key
        