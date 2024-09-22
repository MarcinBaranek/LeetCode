# coding=utf-8

class Solution:
    def isNumber(self, s: str) -> bool:
        if "nf" in s or "an" in s:  # infinity or nan
            return False
        try:
            float(s)
        except ValueError:
            return False
        return True
