class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using heaps

        count_dict = Counter(nums)
        min_heap = []

        for key, freq in count_dict.items():
            heapq.heappush(min_heap, (freq, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [item[1] for item in min_heap]
        

        