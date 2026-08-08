class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = defaultdict(list)

        for word in strs:
            sword = ''.join(sorted(word))
            ag[sword].append(word)
        
        return list(ag.values())

