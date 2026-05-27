class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        # 1 2 4
        # 10 11 12

        # find out located row first
        row, col = None, None

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                row = mid
                break
        if row is None:
            return False

        # find out located column second
        target_row = matrix[row]
        l_col = 0
        r_col = len(target_row) - 1
        while l_col <= r_col:
            mid = (l_col + r_col) // 2
            if target > target_row[mid]:
                l_col = mid + 1
            elif target < target_row[mid]:
                r_col = mid - 1
            else:
                col = mid
                break
        
        if col:
            return True
        return False