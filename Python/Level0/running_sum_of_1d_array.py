class Solution(object):
    def runningSum(self, nums):
        result = []
        temp = 0
        for i in range(len(nums)):
            
            temp = nums[i] + temp
            result.append(temp)
        return result


s = Solution()
print(s.runningSum([1,2,3,4]))