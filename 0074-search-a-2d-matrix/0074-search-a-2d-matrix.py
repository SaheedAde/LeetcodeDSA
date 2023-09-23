class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int]) -> int:
            L = 0
            R = len(nums) - 1
            while L <= R:
                mid_idx = (L + R) // 2
                mid_el = nums[mid_idx]
                if mid_el == target:
                    return mid_idx

                if mid_el < target:
                    L = mid_idx + 1
                else:
                    R = mid_idx - 1
            return -1

        def rowSearch() -> int:
            LRowIdx = 0
            RRowIdx = len(matrix) - 1
            while LRowIdx <= RRowIdx:
                mid_row_idx = (LRowIdx + RRowIdx) // 2
                mid_row_array = matrix[mid_row_idx]
                
                start_el, end_el = mid_row_array[0], mid_row_array[-1]
                if start_el <= target <= end_el:
                    return mid_row_idx
                
                if target < start_el:
                    RRowIdx = mid_row_idx - 1
                if target > end_el:
                    LRowIdx = mid_row_idx + 1
                    
            return -1
        
        row_idx = rowSearch()
        if row_idx == -1:
            return False
        
        col_idx = search(matrix[row_idx])
        if col_idx == -1:
            return False
        
        return True