class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        composites = {}
        for idx, num in enumerate(nums):
            composite = target - num
            if composite in composites:
                composite_idx = composites[composite]
                if idx == composite_idx:
                    continue
                ans = [idx, composite_idx]
                ans.sort()
                return ans
            composites[num] = idx
        return []
        