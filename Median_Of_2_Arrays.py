class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            (nums1,nums2)=(nums2,nums1)
        m,n=len(nums1),len(nums2) # m<=n
        tot=m+n
        low,high=0,m
        pat1,pat2=None,None
        while low<=high:
            pat1=(low+high)//2 #2
            pat2=(tot)//2-pat1 #0
            pat1_left_max=float('-inf') if pat1==0 else nums1[pat1-1] #2
            pat1_right_min=float('inf') if pat1==m else nums1[pat1] #inf
            pat2_left_max=float('-inf') if pat2==0 else nums2[pat2-1] #-inf
            pat2_right_min=float('inf') if pat2==n else nums2[pat2] #3
            if pat1_left_max>pat2_right_min:
                high=pat1-1
            elif pat2_left_max>pat1_right_min:
                low=pat1+1
            else:
                if tot%2==0:
                    return (max(pat1_left_max,pat2_left_max)+min(pat1_right_min,pat2_right_min))/2
                else:
                    return min(pat1_right_min,pat2_right_min)
            print(nums1[:pat1],nums1[pat1:],nums2[:pat2],nums2[pat2:],low,high,pat1,pat2)
            
                

    


        