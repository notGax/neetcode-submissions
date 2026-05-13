class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            if nums[i] in seen:
                return True
            else:
                seen[num]=i
        return False
