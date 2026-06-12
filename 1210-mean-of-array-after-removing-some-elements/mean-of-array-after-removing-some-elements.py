class Solution:
    def trimMean(self, arr):
        arr.sort()
        remove = len(arr) // 20
        total = sum(arr[remove:len(arr) - remove])
        count = len(arr) - 2 * remove
        return total / float(count)