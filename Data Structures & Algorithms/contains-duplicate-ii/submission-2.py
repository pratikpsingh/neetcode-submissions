class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for index, num in enumerate(nums):
            if num in mapping:
                mapping[num].append(index)
            else:
                mapping[num] = [index]
            if len(mapping[num]) >= 2 and abs(mapping[num][-1] - mapping[num][-2]) <= k:
                return True
        
        return False