class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        running_idx = 0
        available_idx = 0
        while running_idx < len(nums):
            current_el = nums[running_idx]

            if current_el != val:
                nums[available_idx] = current_el
                available_idx += 1

            running_idx += 1

        return available_idx