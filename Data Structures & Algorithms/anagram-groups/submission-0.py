class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        
        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string in store:
                store[sorted_string].append(string)
            else:
                store[sorted_string] = [string]

        return list(store.values())