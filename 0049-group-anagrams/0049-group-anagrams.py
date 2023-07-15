from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        alphabet_idx_map = {alph:idx for idx, alph in enumerate(ascii_lowercase)}
        for strng in strs:
            key = [0 for _ in range(len(ascii_lowercase))]
            for char in strng:
                char_idx = alphabet_idx_map[char]
                key[char_idx] += 1
            hashmap[str(key)].append(strng)
            
        return [value for value in hashmap.values()]
            
        