class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency Counter using a Min-Heap for Top K Elements
        import heapq
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i]+=1
        heap = []
        for j in count:
            #Push values and frequencies into the heap as a tuple
            heapq.heappush(heap,(count[j],j))
            #Pop smallest element based off frequency 
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
        # Time Complexity: O(mlog(k))
        # Space Complexity: O(m + n)