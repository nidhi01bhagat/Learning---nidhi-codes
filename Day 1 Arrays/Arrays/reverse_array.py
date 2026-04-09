
# Problem: Reverse Array
# Approach: Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_array(arr):
    left = 0                      # pointer to first element
    right = len(arr) - 1          # pointer to last element
    
    while left < right:           # run until pointers meet
        arr[left], arr[right] = arr[right], arr[left]   # swap values
        
        left += 1                 # move left pointer forward
        right -= 1                # move right pointer backward
        
    return arr                    # return reversed array


# Example usage
arr = [1, 2, 3, 4]
print(reverse_array(arr))   # Output: [4, 3, 2, 1]
