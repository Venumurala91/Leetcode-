class Solution:
    def reverseWords(self, s: str) -> str:
        c=s.split()[::-1]

        return (' '.join(c))