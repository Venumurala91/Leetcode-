class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""

        for i in s:
            if i.isalnum():
                c+=i
            
            
        
       
        if c.lower() == c.lower()[::-1]:
            return True
        
        return False
                
        
       