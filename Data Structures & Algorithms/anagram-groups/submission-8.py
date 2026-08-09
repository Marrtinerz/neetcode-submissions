from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for string in strs:
            count = [0]*26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)

            store[key].append(string)
        
        return list(store.values())