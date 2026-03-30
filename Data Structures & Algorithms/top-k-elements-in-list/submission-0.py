class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i]+=1
        heap = []
        for j in count.keys():
            heapq.heappush(heap,(count[j],j))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]