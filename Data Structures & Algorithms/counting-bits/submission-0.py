class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            n = i
            while n > 0:
                count += (n % 2)
                n //= 2
            result.append(count)
        return result
        