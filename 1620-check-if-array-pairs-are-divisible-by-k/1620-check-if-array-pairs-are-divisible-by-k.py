class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        remainder_count = Counter(x % k for x in arr)
      
        # Check if the number of elements that are divisible by k is even
        if remainder_count[0] % 2 != 0:
            return False
      
        # Check if each non-zero remainder has a complementary count of elements
        # Such that remainder + complementary = k
        # The counts of remainder and its complementary need to be the same
        for remainder in range(1, k):
            if remainder_count[remainder] != remainder_count[k - remainder]:
                return False
              
        # All checks have passed, hence return True
        return True