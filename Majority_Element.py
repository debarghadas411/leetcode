class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        temp={}
        max_occ=0
        max_occ_ele=None
        for i in A:
            temp[i]=temp.get(i,0)+1
            if max_occ<temp[i]:
                max_occ=temp[i]
                max_occ_ele=i
        return max_occ_ele