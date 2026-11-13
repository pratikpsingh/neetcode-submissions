class Solution:
    def hammingWeight(self, n: int) -> int:
        # count = 0
        # while n > 0:
        #     count += (n % 2)
        #     n //= 2
        # return count
        
        count = 0
        while n > 0:
            n &= (n -1)
            count += 1
        return count