class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_value = max(candies)
        max_result = 0
        for i in range(len(candies)):
            if   max_value <= candies[i] + extraCandies:
                result.append(True)
            else:
                result.append(False)
                    
        return result
    
