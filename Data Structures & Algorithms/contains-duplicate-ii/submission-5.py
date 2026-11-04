class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for index, num in enumerate(nums):
            if num in mapping:
                if abs(mapping[num] - index) <= k:
                    return True
            mapping[num] = index
        
        return False