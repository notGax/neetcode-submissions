class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri=""

        def isalphanum(c):
            if("a"<= c <= "z") or ("A"<= c <= "Z") or ("0" <= c <= "9"):
                return c

        for c in s:
            if isalphanum(c):
                stri += c.lower()
        return stri == stri[::-1]
