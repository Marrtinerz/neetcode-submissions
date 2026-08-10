class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first approach: brute force
        count_dict = Counter(nums)
        num_list = [(freq, key) for key, freq in count_dict.items()]
        num_list.sort(reverse=True)
        return [item[1] for item in num_list[:k]]


        