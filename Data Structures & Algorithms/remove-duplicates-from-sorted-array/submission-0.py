class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 1  # position to place the next unique number

        for j in range(1,len(nums)):
            if nums[j] != nums[j - 1]:  # found a new unique number
                nums[i] = nums[j]       # place it at index i
                i += 1                  # move i forward

        return i