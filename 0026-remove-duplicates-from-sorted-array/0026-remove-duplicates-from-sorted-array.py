class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        unique_count = 1
        last_seen = nums[0]
        while i <= len(nums) - 1:
            curr = nums[i]
            if curr == last_seen:
                nums[i] = float(inf)
            else:
                last_seen = curr
                unique_count += 1

            i += 1 
        
        nums.sort()
            
        return unique_count
                
        
        