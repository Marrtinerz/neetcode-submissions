class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        store = Counter(nums)

        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        numbers = list(store.items())

        numbers.sort(reverse=True, key=lambda x:x[1])

        output = []

        for i in range(k):
            output.append(numbers[i][0])

        return output

