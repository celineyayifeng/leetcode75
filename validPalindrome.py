import re 
class Solution(object):
    def isPalindrome(self, s):
        
        # lowercase and remove all non-alphanumeric characters
        s = s.lower()
        stripped_s = re.sub(r'\W','',s)
        print(stripped_s)
        
        
        j = -1  #end
        #i = 0 #start
        
        for i in range(0,len(stripped_s)/2):  #stop at the middle
            
            print('the character at i: ' + stripped_s[i])
            print('the character at j: ' + stripped_s[j])
            
            if stripped_s[i] != stripped_s[j]:
                return False 
            else: #remember to increment
                #i = i+1
                j = j-1
                
        return True
        
class Solution(object):
    def isPalindrome(self, s):
        
        # lowercase and remove all non-alphanumeric characters
        s_lower = s.lower()
        stripped_s = re.sub(r'\W','',s_lower)
        print(stripped_s)
        
        j = len(stripped_s) - 1
        i = 0 
        
        while i < j: 
            
            if stripped_s[i] != stripped_s[j]:
                return False 
            else: 
                i = i + 1
                j = j - 1
        return True

    
