class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        @return true
        """

        original = str(x)

        reverted_number = original[::-1]

        return original == reverted_number