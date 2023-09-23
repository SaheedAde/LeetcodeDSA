# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n
        while L <= R:
            my_guess = (L + R) // 2
            response = guess(my_guess)
            if response == -1:
                R = my_guess - 1
            elif response == 1:
                L = my_guess + 1
            else:
                break
                
        return my_guess
        