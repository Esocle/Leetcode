class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''.join(map(str, digits))
        temp = int(temp)
        temp += 1
        n_list = list(map(int, str(temp)))
        
        return n_list