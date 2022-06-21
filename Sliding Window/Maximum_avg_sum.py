class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        l=0
        h=0
        mx=-10000007
        sumx=0
        avg=0
        
        while(h<len(nums)):
            sumx+=nums[h]
            if h-l+1<k:
                h+=1
            elif h-l+1==k:
                avg=sumx/k
                mx=max(mx,avg)
                sumx-=nums[l]
                l+=1
                h+=1
        return mx
            
        
            
        
