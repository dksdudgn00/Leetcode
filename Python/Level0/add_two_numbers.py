class LinkNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    # def len(self):
    #     return len(self.val)
    
    # # def reverse(self):
    # #     result = []
    # #     for i in range(len(self.val),-1,-1):
    # #         result.append(self.val[i])
    # #     return result
        
    # def add(self, val):
    #     self.val = val
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # l1 = LinkNode([2,4,3])
        # l2 = LinkNode([5,6,4])
        cur = LinkNode()
        carry = 0
        
        result = []
        while l1 and l2:
            carry, val = divmod(l1.val+l2.val+carry, 10)
            l1 = l1.next
            l2 = l2.next
            cur.next = LinkNode(val)
            cur = cur.next
            
        l4 = l1 if l1 else l2
        
            
        # temp = 0
        # temp2 = 0
        # for i in range(len(l1)-1,-1,-1):
        #     if l1[i].val + l2[i].val >= 10:
        #         temp = int(str(l1[i].val + l2[i].val)[0])
        #         temp2 = int(str(l1[i].val + l2[i].val)[1])
                
        #     result.append(LinkNode(l1[i].val + l2[i].val + temp + temp2))
        # result = LinkNode(0)
        
        # for i in range(len(l1)):
        #     result.add(l1[i] + l2[i])
        
        return result

# s = Solution()
# result = s.addTwoNumbers(LinkNode([2,4,3]),LinkNode([5,6,4]))
# print(result)
# print(s.addTwoNumbers([LinkNode(2), LinkNode(4), LinkNode(3)],
#                         [LinkNode(5), LinkNode(6), LinkNode(4)]))
            
s = Solution()
print(s.addTwoNumbers([LinkNode(2), LinkNode(4), LinkNode(3)],
                      [LinkNode(5), LinkNode(6), LinkNode(4)]))