class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(len(nums1)):
            if nums1[i]==0 and j<n:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                j+=1

            
        

        nums1.sort()

        








