class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        while people[right]+people[left] > limit and left <= right:
            count +=1
            right -=1
        
        while left<=right:
            count +=1
            left +=1
            right -=1
        
        return count