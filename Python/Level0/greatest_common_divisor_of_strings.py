class Solution(object):
    def gcdOfStrings(self, str1, str2):
        result = ""
        temp = False
        temp_str = ""
        length = len(str2) if len(str1) > len(str2) else len(str1)
        for i in range(length):
            if str1[i] == str2[i]:
                temp = True
            else:
                temp = False
        if temp and len(str1) > len(str2):
            for i in range(len(str2)):
                if temp_str == str2[i]:
                    break
                temp_str = str2[i]
                result += temp_str
            return result
        elif temp and len(str2) > len(str1):
            for i in range(len(str1)):
                if temp_str == str1[i]:
                    break
                temp_str = str1[i]
                result += temp_str
            return result
        else:
            return ""
            
        
c = Solution()
print(c.gcdOfStrings("ABABAB", "ABAB"))