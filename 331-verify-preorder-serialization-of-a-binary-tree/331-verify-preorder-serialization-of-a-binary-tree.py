class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        temp = preorder.split(',')
        cnt = 1
        for e in temp:
            if cnt == 0:
                return False
            if e == '#':
                cnt -= 1
            else:
                cnt += 1
        return True if cnt == 0 else False
        