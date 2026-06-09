class Solution(object):
    def maximumWealth(self, accounts):
        result = []
        temp = 0
        for i in accounts:
            temp = 0

            for j in i:
                temp += j
            result.append(temp)
            
        result.sort()
        return result[len(result)-1]

s = Solution()
print(s.maximumWealth([[6,59,64,19,30,76,71,86,90,25,56,17,19,
                        72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]))