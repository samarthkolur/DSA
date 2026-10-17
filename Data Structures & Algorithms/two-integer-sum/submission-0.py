class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for ind, num in enumerate (nums):
            if target - num in freq.keys():
                return [freq[target - num], ind]
            else:
                freq[num] = ind
        return []