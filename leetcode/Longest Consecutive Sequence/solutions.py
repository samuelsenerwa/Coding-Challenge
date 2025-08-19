#!/usr/bin/python

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Convert to set for O(1) lookup
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update maximum length found
                max_length = max(max_length, current_length)
        
        return max_length
    

# Test with the provided test cases
def test_longest_consecutive():
    solution = Solution()
    
    test_cases = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [1, 0, 1, 2]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        result = solution.longestConsecutive(nums)
        print(f"Test Case {i}:")
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print()
    
    # Additional edge cases
    print("Additional test cases:")
    print(f"Empty array: {solution.longestConsecutive([])}")
    print(f"Single element: {solution.longestConsecutive([1])}")
    print(f"All duplicates: {solution.longestConsecutive([1, 1, 1, 1])}")
    print(f"No consecutive: {solution.longestConsecutive([1, 3, 5, 7])}")

# Run tests
if __name__ == "__main__":
    test_longest_consecutive()