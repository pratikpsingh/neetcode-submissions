class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            required = target - value
            if required in seen:
                return [seen[required], index]
            seen[value] = index

        return [-1, -1]