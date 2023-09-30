class Solution:
    def findKthLargestBruteForce(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestBruteForce(nums, k)
        