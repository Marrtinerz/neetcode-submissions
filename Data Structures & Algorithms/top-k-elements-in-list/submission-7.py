class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        count_dict = Counter(nums)
        count_list = list(count_dict.items())
        count_list.sort(reverse=True, key=lambda x: x[1])
        return [item[0] for item in count_list[:k]]