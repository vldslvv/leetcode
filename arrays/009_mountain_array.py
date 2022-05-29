
class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False

        passed_summit = False

        for i in range(0, len(arr) - 1):
            # first half, search for summit
            if not passed_summit and arr[i] < arr[i + 1]:
                continue

            if i > 0 and not passed_summit and arr[i] > arr[i + 1]:
                passed_summit = True
                continue
            
            if passed_summit and arr[i] > arr[i + 1]:
                continue
            
            return False

        return passed_summit
        