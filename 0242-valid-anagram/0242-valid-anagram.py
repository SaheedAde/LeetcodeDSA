from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        hashmap = defaultdict(int)
        for char_s, char_t in zip(s, t):
            hashmap[char_s] += 1
            hashmap[char_t] -= 1

        for char in hashmap:
            if hashmap[char]:
                return False

        return True
        