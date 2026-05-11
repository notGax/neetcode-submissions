class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and (nums[i]==nums[j]):
                    return True
        return False   