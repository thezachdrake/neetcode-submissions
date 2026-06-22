class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new: list[int] = []
        for idx in range(len(arr)-1):
            new += [max(arr[idx+1:])]
        new += [-1]
        return new
