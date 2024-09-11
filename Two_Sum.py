class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted=sorted(nums)
        n=len(nums_sorted)
        pair=None
        end=False
        for i in range(n):
            low=i
            high=n-1
            while low<=high and end==False:
                mid=(low+high)//2
                print(i,mid,nums_sorted[i],nums_sorted[mid],nums_sorted[i]+nums_sorted[mid],target)
                if (nums_sorted[mid]+nums_sorted[i])==target:
                    pair=[nums_sorted[i],nums_sorted[mid]]
                    end=True
                elif (nums_sorted[mid]+nums_sorted[i])<target:
                    low=mid+1
                elif (nums_sorted[mid]+nums_sorted[i])>target:
                    high=mid-1
                    
        output=[]
        for x in pair:
            for i in range(n):
                if nums[i]==x and i not in output:
                    output.append(i)
                    break
        return output