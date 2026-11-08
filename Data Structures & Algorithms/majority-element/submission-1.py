class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, element = 0, None
        for num in nums:
            if element is None:
                element = num
                count += 1
            elif num == element:
                count += 1
            elif num != element:
                count -= 1
                if count == 0:
                    element = None
            
        return element

        