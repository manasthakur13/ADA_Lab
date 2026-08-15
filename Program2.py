from typing import List

class Sort:
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append whatever elements are left over
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def quick_sort(self, arr: List[int]) -> List[int]:
        nums = arr.copy()
        self._quick_sort_in_place(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort_in_place(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_idx = self._partition(arr, low, high)
            self._quick_sort_in_place(arr, low, pivot_idx - 1)
            self._quick_sort_in_place(arr, pivot_idx + 1, high)

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]  # Lomuto partition scheme using the last element
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place the pivot directly after the smaller elements partition
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    sorter = Sort()
    test_data = [38, 27, 43, 3, 9, 82, 10]

    print("Merge Sort:", sorter.merge_sort(test_data))
    print("Quick Sort:", sorter.quick_sort(test_data))