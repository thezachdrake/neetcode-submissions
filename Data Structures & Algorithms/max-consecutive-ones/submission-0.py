class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_run: int = 0
        count: int = 0
        for num in nums:
            if num == 0:
                best_run = count if count > best_run else best_run
                count = 0
                continue
            else:
                count = count + 1
                best_run = count if count > best_run else best_run
        return best_run