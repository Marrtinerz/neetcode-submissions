class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        num_list = [(-freq, key) for key, freq in count_dict.items()]
        heapq.heapify(num_list)
        output = []
        for i in range(k):
            output.append(heapq.heappop(num_list)[1])


        return output
