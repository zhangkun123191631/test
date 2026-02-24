from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    使用冒泡排序对整数列表进行升序排序。
    返回一个新列表，不修改原列表。
    """
    arr = nums.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        # 每一轮把当前未排序部分的最大值“冒泡”到末尾
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 如果这一轮没有交换，说明已经有序，可提前结束
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("原数组:", sample)
    print("排序后:", bubble_sort(sample))

    sample2 = [3, -1, 3, 0, -5, 8, 8]
    print("原数组2:", sample2)
    print("排序后2:", bubble_sort(sample2))
