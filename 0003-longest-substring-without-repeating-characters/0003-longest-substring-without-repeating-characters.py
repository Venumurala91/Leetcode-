class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                c=''
                i=0
                m=0
                j=0

                if len(s)==1:
                    return len(s)

                while i<len(s) and j<len(s):
                    if s[j]  not in c:
                        c+=s[j]
                        j+=1
                        m=max(len(c),m)
                    
                    else:
                        m=max(len(c),m)
                        i+=1
                        j=i
                        c=""
                

                return m

            
            













        # l=[]
        # c=""
        # m=0

        # dvdf

        # if len(s)==1:
        #         return len(s)
            
        # for i in s:
        #     if i not in c:
        #         c+=i
            
        #     else:
        #         l.append(c)
        #         c=""
        #         c+=i
        #     l.append(c)
        
        # if len(l)==0:
        #     return len(c)
        # for i in range(len(l)):
        #     if len(l[i])>m:
        #         m=len(l[i])
        
        # return m 
                
                
            
            
       

        