class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result_l1 = []
        result_l2 = []
        sliced_str = ""
        result_int = 0
        result_int2 = 0
        for i in range(len(l1)-1,-1,-1):
            result_l1.append(l1[i])
        for i in range(len(l2)-1,-1,-1):
            result_l2.append(l2[i])

        final_result = []
        for i in range(len(result_l1)):
            for j in range(len(result_l2)):
                if i == j:
                    if result_l1[i] + result_l2[j] >= 10:
                        num_str = str(result_l1[i] + result_l2[j])
                        sliced_str = num_str[1]
                        result_int = int(sliced_str)
                        result_int2 = int(num_str[0])
                        final_result.append(result_int)
                        continue
                    final_result.append(result_l1[i] + result_l2[j] + result_int2)
                    break
        
        return final_result


a = Solution()
print(a.addTwoNumbers([2,4,3],[5,6,4]))
        
