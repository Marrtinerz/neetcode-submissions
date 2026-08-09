class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for string in strs:
            count = [0]*26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)

            if key in store:
                store[key].append(string)
            else:
                store[key] = [string]
        
        return list(store.values())