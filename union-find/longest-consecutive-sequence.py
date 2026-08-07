class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        seq = 0
        if len(nums)==0:
            return 0
        for num in n:
            count = 1
            if num-1 in n:
                continue
            else:
                while num+1 in n:
                    count +=1
                    num+=1
                if count>seq:
                    seq = count
        return seq