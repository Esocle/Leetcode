class Solution:
    def mySqrt(self, x: int) -> int:
        div = 0
        while ((div + 1) * (div + 1) <= x):
            div += 1
        return div