class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        store = Counter(nums)
        numbers = list(store.items())
        numbers.sort(reverse=True, key=lambda x: x[1])

        return [item[0] for item in numbers[:k]]

