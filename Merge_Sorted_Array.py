class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        pos=(m+n)-1
        while i>=0 and j>=0:
            if nums1[i]<=nums2[j]:
                nums1[pos]=nums2[j]
                j-=1
            else:
                nums1[pos]=nums1[i]
                i-=1
            pos-=1
        if i<0:
            nums1[0:pos+1]=nums2[0:j+1]