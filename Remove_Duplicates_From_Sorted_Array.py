class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        pos=0
        n=len(nums)
        if n==1:
            return 1
        while i<n:
            if nums[pos]!=nums[i]:
                pos+=1
                nums[pos]=nums[i]
            i+=1
        return pos+1