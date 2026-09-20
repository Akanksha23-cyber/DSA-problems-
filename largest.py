<<<<<<< HEAD
class Solution():
    def largest(self,arr):
        largest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        return largest
=======
Brute force 

class Solution():
    def largest(self,arr):
        n = len(arr)
        arr.sort()
        return arr[n-1]
