class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = set('abcdefghijklmnopqrstuvwxyz0123456789')
        
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i].lower() not in alpha:
                i += 1
                continue
            if s[j].lower() not in alpha:
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
