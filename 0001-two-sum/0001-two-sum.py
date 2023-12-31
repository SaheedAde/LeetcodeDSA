class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        composites = {}
        for idx, num in enumerate(nums):
            composite = target - num
            if composite in composites:
                composite_idx = composites[composite]
                return [idx, composite_idx] if idx < composite_idx else [composite_idx, idx]
            composites[num] = idx
        return []