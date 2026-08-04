class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen :
                seen[nums[i]] +=1
            else:
                seen[nums[i]] = 1
        sorte = list(sorted(seen, key = seen.get, reverse = True))
        l1 = []
        for i in range(k):
            l1.append(sorte[i])
        return l1
        
           
            
            
         
             
        
        