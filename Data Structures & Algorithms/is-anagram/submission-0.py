class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = sorted(list(s.lower()))
        T = sorted(list(t.lower()))

        if S == T:
            return True
        return False

