class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_index = -1
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == val and swap_index == -1:
                swap_index = i
            elif nums[i] != val:
                if swap_index != -1:
                    nums[swap_index] = nums[i]
                    swap_index += 1
                count += 1
            i += 1

        return count