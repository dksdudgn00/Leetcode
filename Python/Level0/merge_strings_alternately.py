class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        result_str = ""
        length = len(word1) if len(word1) > len(word2) else len(word2)
        # length2 = len(word1) if len(word1) > len(word2) else len(word2)
        # for i in range(len(word1)):
        #     result.append(word1[i])
        # for i in range(len(word2)):
        #     result.append(word2[i])

        # for i in range(length2):
        #     if len(word1) > len(word2):
        #         if i > len(word1):
        #             result_str += word1[i]
        #         else:
        #             result_str += word1[i]
        #             result_str += word2[i]
        #     elif len(word2) > len(word1):
        #         if i > len(word2):
        #             result_str += word2[i]
        #         else:
        #             result_str += word1[i]
        #             result_str += word2[i]

        # 긴 문자열만큼 반복한다.
        for i in range(length):
            if not i >= len(word1):
                result_str += word1[i]
            if not i >= len(word2):
                result_str += word2[i]
            
                
        
        return result_str

s = Solution()
print(s.mergeAlternately("ab", "pqrs"))