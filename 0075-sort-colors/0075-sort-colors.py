class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_cnts = defaultdict(int)
        for num in nums:
            num_cnts[num] += 1

        i = 0
        for n in [0, 1, 2]:
            cnts = num_cnts[n]
            while cnts:
                nums[i] = n
                i += 1
                cnts -= 1
        