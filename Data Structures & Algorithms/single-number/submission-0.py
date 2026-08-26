class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        duplicate = set()
        for i in nums:
            if i in seen:
                duplicate.add(i)
            else:
                seen.add(i)
        for i in seen: 
            if i not in duplicate:
                return i