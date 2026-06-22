class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array: list[int] = []
        for idx, num in enumerate(arr):
            if idx != len(arr) - 1:
                split = arr[idx+1:]
                new_array.append(max(split))
            else:
                new_array.append(-1)
        return new_array
