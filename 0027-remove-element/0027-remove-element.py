class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         running_idx = 0
#         available_idx = None
#         while running_idx < len(nums):
#             current_el = nums[running_idx]
            
#             if current_el != val:
#                 if available_idx is None:
#                     running_idx += 1
#                     continue

#                 nums[available_idx] = current_el
#                 available_idx += 1
#                 running_idx += 1
#                 continue

#             if current_el == val:
#                 if available_idx is None:
#                     available_idx = running_idx
#                 running_idx += 1
#                 continue

#         return available_idx


        running_idx = 0
        available_idx = 0
        while running_idx < len(nums):
            current_el = nums[running_idx]

            if current_el != val:
                nums[available_idx] = current_el
                available_idx += 1
                running_idx += 1
                continue

            running_idx += 1
            continue

        return available_idx