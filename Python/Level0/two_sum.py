class Solution:
    def twoSum(self, num, target):
        # 이중 포문
        result = []
        for i in range(0, len(num)-1):
            first = num[i]
            if len(result) > 0:
                break
            for j in range(i, len(num)):
                if first + num[j] == target and i != j:
                    result.append(num.index(first))
                    result.append(j)
                    break

        return result

    


solve = Solution()
result = solve.twoSum([3,3], 6)
print(result)
