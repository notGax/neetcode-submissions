class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:#checking if its sorted or not on the left of mid
                if nums[left]<= target < nums[mid]:#checking if target is between left and mid
                    right=mid-1
                else:
                    left=mid+1
            if nums[right]>=nums[mid]:
                if nums[right]>=target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1