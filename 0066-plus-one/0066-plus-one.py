class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        c=''
        for i in arr:
            c+=str(i)

        
        s=int(c)+1
        
        s=str(s)
        a=[0]*len(str(s))

        for i in range(len(str(s))):
            a[i]=int(s[i])
    

        return a
            
        

        