class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums + nums
        
        return [num for _ in range(2) for num in nums]