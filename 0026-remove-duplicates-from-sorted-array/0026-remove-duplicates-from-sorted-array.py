class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r_idx = 1 # scanning through ptr
        l_idx = 1 # Available location ptr
        while r_idx < len(nums):
            current_element = nums[r_idx]
            previous_element = nums[r_idx - 1]
            is_duplicate = current_element == previous_element
            if not is_duplicate:
                # Put current element in the available idx and shift both available location and current index
                nums[l_idx] = current_element
                l_idx += 1

            r_idx += 1
            
        return l_idx
