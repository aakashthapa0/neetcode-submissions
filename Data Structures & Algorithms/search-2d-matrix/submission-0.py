class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2

            value = matrix[mid // columns][mid % columns]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False