class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        
        num_heap = []

        for key, freq in count_dict.items():
            heapq.heappush(num_heap, (freq, key))

            if len(num_heap) > k:
                heapq.heappop(num_heap)
            
        return [item[1] for item in num_heap]