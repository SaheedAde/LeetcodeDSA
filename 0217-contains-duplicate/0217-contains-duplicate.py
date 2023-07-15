class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        last_seen = None
        for num in nums:
            if num == last_seen:
                return True
            last_seen = num
        return False