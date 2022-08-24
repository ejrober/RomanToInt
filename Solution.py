class Solution:

    def romanToInt(self, s: str) -> int:
        if len(s) < 1:
            return 0

        elif s[len(s)-1] == "I":

            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 1)
        
        elif s[len(s)-1] == "V":
            if len(s) >1 and s[len(s)-2] == "I":

                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 4)
            
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 5)
        
        elif s[len(s)-1] == "X":
            if len(s) >1 and s[len(s)-2] == "I":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 9)
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 10)
        
        elif s[len(s)-1] == "L":
            if len(s) >1 and s[len(s)-2] == "I":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 49)
            elif len(s) >1 and s[len(s)-2] == "V":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 45)
            elif len(s) >1 and s[len(s)-2] == "X":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 40)
            
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 50)
        
        elif s[len(s)-1] == "C":
            if len(s) >1 and s[len(s)-2] == "I":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 99)
            elif len(s) >1 and s[len(s)-2] == "V":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 95)
            elif len(s) >1 and s[len(s)-2] == "X":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 90)
            
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 100)
        
        elif s[len(s)-1] == "D":
            if len(s) >1 and s[len(s)-2] == "I":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 499)
            elif len(s) >1 and s[len(s)-2] == "V":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 495)
            elif len(s) >1 and s[len(s)-2] == "X":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 490)
            elif len(s) >1 and s[len(s)-2] == "L":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 450)
            elif len(s) >1 and s[len(s)-2] == "C":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 400)
            
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 500)
        
        elif s[len(s)-1] == "M":
            if len(s) >1 and s[len(s)-2] == "I":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 999)
            elif len(s) >1 and s[len(s)-2] == "V":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 995)
            elif len(s) >1 and s[len(s)-2] == "X":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 990)
            elif len(s) >1 and s[len(s)-2] == "L":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 950)
            elif len(s) >1 and s[len(s)-2] == "C":
                
                return int((Solution.romanToInt(self, s[0:len(s)-2])) + 900)
            
            return int((Solution.romanToInt(self, s[0:len(s)-1])) + 1000)
        
        else:
            return 0