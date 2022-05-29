
def find_max(arr, start_id):
    if start_id >= len(arr):
        return -1, -1
    m = arr[start_id]
    m_id = start_id
    for i in range(start_id + 1, len(arr)):
        if arr[i] > m:
            m = arr[i]
            m_id = i
    return m, m_id


class Solution:
    def replaceElements(self, arr):
        if len(arr) == 0:
            return arr
        
        # For each i-th element, find max and max_id to the right
        max_el, max_id = find_max(arr, 1)
        for i in range(len(arr) - 1):
            if i >= max_id:
                max_el, max_id = find_max(arr, i + 1)
            
            arr[i] = max_el
        
        # Write last element
        arr[len(arr) - 1] = -1
        return arr
