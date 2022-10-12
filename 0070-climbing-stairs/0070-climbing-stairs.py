class Solution:
    def climbStairs(self, n: int) -> int:
        # 피보나치 수열
        def fib(n):
            fibList=[1, 1]
            if n == 1:
                return 1
            elif n == 2:
                return 2
            for i in range(2,n):
                fibList.append( fibList[i-1] + fibList[i-2] )
            return fibList
        
        temp = fib(n)
        
        try:
            return temp[-2] + temp[-1]
        except:
            return temp