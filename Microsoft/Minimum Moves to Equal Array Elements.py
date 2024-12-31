class Solution(object):
    def minMoves2(self, nums):
        nums.sort()

        mid = nums[len(nums)//2]
        count = 0
        for num in nums:
            count += abs(mid-num)
        
        return count
