class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [None] * (2 * len(nums))
        # for idx in range(len(ans)):
        #     ans[idx] = nums[idx%len(nums)]
        # return ans
        return [nums[idx%len(nums)] for idx in range(2 * len(nums))]
        