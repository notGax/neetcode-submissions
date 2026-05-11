class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pzero=0
        ptwo=len(nums)-1
        i=0

        def swap(x,y):
            tmp=nums[x]
            nums[x]=nums[y]
            nums[y]=tmp

        while i<=ptwo:
            if nums[i]==0:
                swap(pzero,i)
                pzero+=1

            elif nums[i]==2:
                swap(ptwo,i)
                ptwo-=1
                i-=1
            i+=1

        
