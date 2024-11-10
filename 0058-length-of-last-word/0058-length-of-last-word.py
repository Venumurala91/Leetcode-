class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=[]
        c=""
        for i in s:
            if i!=" ":
                c+=i
            
            elif c:
                d.append(c)
                c=""
            
        if c:
            d.append(c)    
        # print(d)
        return len(d[-1])