class Solution(object):
    def leftRightDifference(self, nums):
        leftsum = []
        rightsum = []
        result = []
        sum = 0
        for i in range(len(nums)):
            sum = 0
            if i == 0:
                leftsum.append(0)
            else:
                for j in range(i):
                    sum += nums[j]
                leftsum.append(sum)
        sum = 0
        nums.reverse()
        for i in range(len(nums)):
            sum = 0
            if i == 0:
                rightsum.append(0)
            else:
                for j in range(i):
                    sum += nums[j]
                rightsum.append(sum)
        rightsum.reverse()
        for i in range(len(nums)):
            if leftsum[i] - rightsum[i] < 0:
                result.append(-(leftsum[i] - rightsum[i]))
            else:
                result.append((leftsum[i] - rightsum[i]))
                
        return result
            
        
s = Solution()
print(s.leftRightDifference([10,4,8,3]))