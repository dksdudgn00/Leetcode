
def gcd(a, b):
    while b:
        a, b = b, a %  b
    return a
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        result = ""
        if str1+str2 != str2+str1:
            return ""
        count = gcd(len(str1), len(str2))
        
        for i in range(count):
            result += str1[i]

        return result
        

            

            



        
c = Solution()
print(c.gcdOfStrings("ABABAB", "AB"))