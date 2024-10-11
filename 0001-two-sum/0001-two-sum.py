class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        


        c={}
        for i in range(len(arr)):
            c[i]=arr[i]

        arr.sort()
        i=0
        j=len(arr)-1

        if len(arr)==2 and arr[0]+arr[1]==target:
            return [0,1]

        while i<j:
            if arr[i]+arr[j]==target:
                break
            elif arr[i]+arr[j]>target:
                j-=1
            else:
                i+=1
        
        f=True
        for k in range(len(arr)):
            if c[k]==arr[i] and f:
                p=k
                f=False
            elif c[k]==arr[j]:
                q=k
        
        return p,q


        







        
        