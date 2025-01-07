class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if len(s)==1:
            return dic[s[0]]

        SUM=0
        visited=False
        for i in range(len(s)-1):
            if dic[s[i+1]]>dic[s[i]]:
                SUM+=int(dic[s[i+1]])-int(dic[s[i]])
                visited=True

            elif not visited:
                SUM+=int(dic[s[i]])
            else:
                visited=False



        
       
        if i<len(s) and dic[s[i+1]]==dic[s[i]]:
            SUM+=int(dic[s[i]])
        
        elif dic[s[i+1]]<dic[s[i]]:
            SUM+=int(dic[s[i+1]])

        


        return SUM 





