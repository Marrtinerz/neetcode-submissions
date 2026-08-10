class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using bucketsort

        count_dict = Counter(nums)

        empty_bucket = [[] for _ in range(len(nums)+1)]

        for key, freq in count_dict.items():
            empty_bucket[freq].append(key)

        result = []
        for i in range(len(nums), -1, -1):
            if empty_bucket[i]:
                # 2. Fix: Loop through individual elements to prevent overflowing past k
                for num in empty_bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
        return result





        

        