class Solution:

    def encode(self, strs: list[str]) -> str:
        # Turn ["hello", "world"] -> "5/hello5/world"
        res = []
        for string in strs:
            res.append(f"{len(string)}/{string}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res_list = []
        index = 0

        # Use a while loop so changing index alters our progress dynamically
        while index < len(s):
            # 1. Find where the delimiter "/" is
            slash_index = s.find("/", index)
            
            # 2. Extract the length of the upcoming string
            str_length = int(s[index:slash_index])
            
            # 3. Jump index past the "/" delimiter
            index = slash_index + 1
            
            # 4. Extract the exact word using slicing
            word = s[index : index + str_length]
            res_list.append(word)
            
            # 5. Move index past the processed word
            index += str_length

        return res_list
