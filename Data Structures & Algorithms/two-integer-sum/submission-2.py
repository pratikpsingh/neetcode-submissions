class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in hash_map:
                return [hash_map[remaining], index]
            hash_map[num] = index

        return [-1, -1]
        