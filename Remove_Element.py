class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos=0
        n=len(nums)-1
        if n<0:
            return 0
        while pos<=n:
            if nums[pos]==val:
                nums[pos],nums[n]=nums[n],nums[pos]
                n-=1
            else:
                pos+=1
            # print(pos,n)
        if pos==0 and nums[pos]==val:
            return 0
        return pos