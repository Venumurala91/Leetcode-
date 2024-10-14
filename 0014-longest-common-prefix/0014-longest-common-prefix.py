class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if len(arr)<=1:
            return arr[0]
        a=len(arr[0])
        
        for i in range(1,len(arr)):
            a=min(a,len(arr[i]))
            while a>0 and arr[0][0:a]!=arr[i][0:a]:
                a-=1
                if a==0:
                    return ""
        
        return arr[0][0:a]



        