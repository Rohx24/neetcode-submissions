class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        t = []
        for i in range(2):
            for j in nums:
                t.append(j)
        return t
