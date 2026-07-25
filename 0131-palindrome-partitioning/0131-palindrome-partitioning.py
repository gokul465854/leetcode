class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            # If we reached the end, store one valid partition
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()      # Backtrack

        backtrack(0)
        return result