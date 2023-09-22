class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid_idx = (L + R) // 2
            mid_el = nums[mid_idx]
            if mid_el == target:
                return mid_idx

            if mid_el < target:
                L = mid_idx + 1
            else:
                R = mid_idx - 1
        return -1
        