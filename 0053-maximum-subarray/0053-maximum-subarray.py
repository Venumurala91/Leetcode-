class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
      
        # Iterate through the remaining elements in the list starting from the second element.
        for num in nums[1:]:
            # Update the current subarray sum. Add the current number to the current sum,
            # or reset it to the current number if the current sum is negative.
            current_sum = max(current_sum + num, num)
          
            # Update the maximum subarray sum if the current subarray sum is greater.
            max_sum = max(max_sum, current_sum)
      
        # Return the maximum subarray sum found.
        return max_sum