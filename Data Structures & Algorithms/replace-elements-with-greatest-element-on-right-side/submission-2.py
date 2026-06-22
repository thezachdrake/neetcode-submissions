class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array: list[int] = []
        for idx in range(len(arr) - 1):
            new_array += [(max(arr[idx+1:]))]
        new_array += [-1]
        return new_array
